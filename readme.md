# 🐍 Python Scripting for VLSI/EDA Automation

This repository contains modular Python scripts designed to automate and support workflows related to **VLSI design**, **simulation**, and **EDA tool usage**. Each subfolder demonstrates a specific scripting concept or Python module with practical use cases.

---

## 📁 Folder Structure

### 🔹 `argparse/`
- Demonstrates how to use the `argparse` module for command-line argument parsing.
- Example use case: Automating Verilog compilation and simulation with command-line inputs.

### 🔹 `Regex/`
- Uses Python `re` module to search and analyze text files.
- Example: Count occurrences of the word `vlsi` in a sample file.

### 🔹 `subprocess/`
- Uses `subprocess` to run external commands like `iverilog`, `vvp`, or `gtkwave`.
- Automates compilation and waveform generation for Verilog designs.

### 🔹 `counter/`
- Contains Verilog files:
  - `bcd_counter.v` — A simple BCD counter module.
  - `bcd_counter_tb.v` — Testbench for simulating the counter.
- Used with scripts in `subprocess/` for testing simulation automation.

### 🔹 `os_module/`
- Demonstrates usage of `os` for directory creation and file handling.
- Example: Dynamically creating folders for organizing scripts or outputs.

---

## ⚙️ Example Script Use Cases

- Automatically compile and simulate Verilog using:
  ```bash
  python run_simulation.py --top counter/bcd_counter.v --tb counter/bcd_counter_tb.v --wave
