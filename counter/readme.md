# BCD Up/Down Counter in Verilog

This project implements a simple **BCD (Binary-Coded Decimal) counter** using Verilog HDL. It supports both **incrementing (up)** and **decrementing (down)** operations within the BCD range `0–9`. A testbench is also included to verify its functionality.

---

## 🔧 Features

- 4-bit BCD counter (`0000` to `1001`)
- Count **up** or **down** on each positive clock edge
- Wraps around:
  - Up from 9 → 0
  - Down from 0 → 9
- Active-high **reset** to zero the counter
- **Testbench** included for simulation

---

## 🧠 Module Description

### `bcd_counter.v`

#### Inputs:
- `clk`: Clock signal
- `reset`: Synchronous active-high reset
- `up`: Count up signal
- `down`: Count down signal

#### Output:
- `count [3:0]`: Current BCD counter value (0–9)

The counter ensures mutual exclusivity between the `up` and `down` signals.

---

## 📁 File Structure

bcd-counter/
│
├── bcd_counter.v # BCD counter module
├── bcd_counter_tb.v # Testbench for simulation
├── bcd_counter.vcd # Waveform dump (after simulation)
└── README.md # Project documentation


---

## 🧪 Simulation Instructions

You can simulate this project using any Verilog simulator. The example below uses **Icarus Verilog** and **GTKWave**.

### Step 1: Compile

iverilog -o counter.vvp bcd_counter.v tb_bcd_counter.v

### Step 2: Run Simulation
vvp counter.vvp

### Step 3: View Waveform (optional)

gtkwave counter.vcd

