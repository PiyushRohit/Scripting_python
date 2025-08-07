import argparse
import subprocess
import os
import sys

# -------------------------------
# Argument Parser Configuration
# -------------------------------
parser = argparse.ArgumentParser(description="Automate Verilog simulation and waveform viewing.")

parser.add_argument('--design', required=True, help='Verilog design file (e.g., bcd_counter.v)')
parser.add_argument('--tb', required=True, help='Testbench file (e.g., bcd_counter_tb.v)')
parser.add_argument('--output', default='sim_out', help='Name of simulation output binary (default: sim_out)')
parser.add_argument('--vcd', default='waveform.vcd', help='VCD waveform output file name (default: waveform.vcd)')
parser.add_argument('--gtkw', help='Optional GTKWave layout file (.gtkw)')

args = parser.parse_args()

# -------------------------------
# Cleanup Previous Outputs
# -------------------------------
if os.path.exists(args.output):
    os.remove(args.output)
if os.path.exists(args.vcd):
    os.remove(args.vcd)

# -------------------------------
# Compile Verilog Design + TB
# -------------------------------
print("🔨 Compiling Verilog files...")
compile_cmd = ['iverilog', '-o', args.output, args.design, args.tb]
compile_result = subprocess.run(compile_cmd, capture_output=True, text=True)

if compile_result.returncode != 0:
    print("❌ Compilation failed:")
    print(compile_result.stderr)
    sys.exit(1)
else:
    print("✅ Compilation successful.")

# -------------------------------
# Run Simulation
# -------------------------------
print("🚀 Running simulation...")
simulate_cmd = ['vvp', args.output]
sim_result = subprocess.run(simulate_cmd, capture_output=True, text=True)

if sim_result.returncode != 0:
    print("❌ Simulation failed:")
    print(sim_result.stderr)
    sys.exit(1)
else:
    print("✅ Simulation output:")
    print(sim_result.stdout)

# -------------------------------
# Launch GTKWave Automatically
# -------------------------------
if not os.path.exists(args.vcd):
    print(f"⚠️ VCD file '{args.vcd}' not found. Cannot open GTKWave.")
    sys.exit(1)

if args.gtkw and os.path.exists(args.gtkw):
    print(f"📂 Launching GTKWave with layout: {args.gtkw}")
    subprocess.run(['gtkwave', args.vcd, args.gtkw])
else:
    print("📂 Launching GTKWave without layout.")
    subprocess.run(['gtkwave', args.vcd])
