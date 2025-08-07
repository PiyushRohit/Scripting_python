import json
import subprocess
import sys
import os
import logging
import re

# -----------------------
# Logging Setup
# -----------------------
def setup_logger(log_level, log_dir):
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, "synthesis_run.log")

    logger = logging.getLogger("synthesis_logger")
    logger.setLevel(getattr(logging, log_level.upper(), logging.INFO))

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(log_file, mode="a")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger

# -----------------------
# Parse Tool Log (Errors, Warnings, Timing)
# -----------------------
def parse_tool_log(log_path, logger):
    if not os.path.exists(log_path):
        logger.warning(f"No tool log found at {log_path}")
        return

    logger.info(f"Parsing tool log: {log_path}")

    errors, warnings, criticals = [], [], []
    timing_violations = []

    with open(log_path, "r", errors="ignore") as f:
        for line in f:
            # Error/Warning/Critical detection
            if re.search(r"\bERROR\b", line, re.IGNORECASE):
                errors.append(line.strip())
            elif re.search(r"\bWARNING\b", line, re.IGNORECASE):
                warnings.append(line.strip())
            elif re.search(r"\bCRITICAL\b", line, re.IGNORECASE):
                criticals.append(line.strip())

            # Timing violation detection
            if re.search(r"slack\s*[:=]\s*-?\d+(\.\d+)?", line, re.IGNORECASE):
                match = re.search(r"-?\d+(\.\d+)?", line)
                if match:
                    slack_value = float(match.group())
                    if slack_value < 0:
                        timing_violations.append(f"Negative Slack: {slack_value} ns")
            if re.search(r"(setup|hold) violation", line, re.IGNORECASE):
                timing_violations.append(line.strip())
            if re.search(r"\bWNS\b\s*<\s*0", line, re.IGNORECASE):
                timing_violations.append("WNS < 0 (Setup violation)")
            if re.search(r"\bTNS\b\s*<\s*0", line, re.IGNORECASE):
                timing_violations.append("TNS < 0 (Multiple violations)")

    # Summary
    logger.info("===== TOOL LOG SUMMARY =====")
    logger.info(f"Errors   : {len(errors)}")
    logger.info(f"Warnings : {len(warnings)}")
    logger.info(f"Critical : {len(criticals)}")
    logger.info(f"Timing Violations: {len(timing_violations)}")

    if errors:
        logger.error("\n".join(errors[:10]))
    if warnings:
        logger.warning("\n".join(warnings[:10]))
    if criticals:
        logger.critical("\n".join(criticals[:10]))
    if timing_violations:
        logger.error("⚠ Timing Issues Detected:")
        logger.error("\n".join(timing_violations[:10]))

# -----------------------
# Main Script
# -----------------------
with open("config.json", "r") as f:
    config = json.load(f)

tool_name = sys.argv[1] if len(sys.argv) > 1 else config["default_tool"]

if tool_name not in config["tools"]:
    print(f"Error: Tool '{tool_name}' not found in config.json")
    sys.exit(1)

tool_config = config["tools"][tool_name]
output_dir = tool_config["output_directory"]

logger = setup_logger(tool_config.get("log_level", "INFO"), output_dir)

cmd = [tool_config["command"]] + tool_config["flags"]

logger.info(f"=== Running {tool_name.upper()} Synthesis ===")
logger.info(f"Command: {' '.join(cmd)}")
logger.info(f"Output Directory: {output_dir}")

try:
    subprocess.run(cmd, check=True)
    logger.info("✅ Synthesis completed successfully.")
except subprocess.CalledProcessError as e:
    logger.error(f"❌ Synthesis failed with exit code {e.returncode}")
except FileNotFoundError:
    logger.error(f"❌ Tool '{tool_config['command']}' not found in PATH")

# -----------------------
# Parse Tool Log File from config.json
# -----------------------
log_file_path = os.path.join(output_dir, tool_config["tool_log"])
parse_tool_log(log_file_path, logger)
