#  Verilog Simulation Automation Tool

A Python script to streamline Verilog simulation using **Icarus Verilog (iverilog)** and **GTKWave**, with support for custom waveform layouts, VCD generation, and testbench automation.

---

##  Problem Statement

Simulating Verilog designs often involves repetitive tasks like:

- Compiling design and testbench files with `iverilog`
- Running simulations with `vvp`
- Cleaning up intermediate files
- Opening waveforms in GTKWave with or without a layout

Doing this manually for each simulation wastes time and can lead to mistakes or inconsistent analysis.

---

## ✅ Solution

This script automates the entire flow:
- Cleans up old binaries and waveforms
- Compiles both the design and testbench using `iverilog`
- Runs simulation with `vvp`
- Optionally opens the waveform in **GTKWave** with a `.gtkw` layout

Perfect for **students**, **RTL engineers**, and **FPGA/ASIC hobbyists**.

---

## 🔧 Requirements

- Python 3.x
- [Icarus Verilog](http://iverilog.icarus.com/)
- [GTKWave](http://gtkwave.sourceforge.net/)

---

## ⚙️ How It Works

```bash
python simulate.py --design bcd_counter.v --tb bcd_counter_tb.v --wave
