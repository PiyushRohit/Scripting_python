# ⏱️ Timing Report Violation Parser

This Python script automates the parsing of STA (Static Timing Analysis) reports to extract **setup** and **hold** timing violations. It generates a clean summary in CSV format and logs key actions for traceability.

---

## 🧩 Problem Statement

In VLSI and ASIC design, STA tools generate long textual timing reports. Manually identifying and categorizing **setup** and **hold** violations from these reports can be:

- Time-consuming 🕒  
- Error-prone ❌  
- Hard to document or analyze systematically 📄  

---

## ✅ Solution

This script automates the entire process by:

- Scanning through the timing report line by line  
- Identifying and extracting lines that mention `setup` or `hold` violations  
- Writing the categorized violations into a structured **CSV file**  
- Logging all activity to a **log file** for reproducibility and debugging

This improves productivity and ensures consistency in STA validation workflows.

---

## 📌 Features

- ✅ **Parse STA reports** for `setup` and `hold` violations  
- 📄 **Log activities** using Python’s `logging` module  
- 📊 **Export violations** into a clean `CSV` format  
- 🧪 Modular and easy to integrate into EDA/STA flows  

---

## 📂 File Structure

├── timing_report.txt # Input STA report
├── violations_summary.csv # Output CSV file
├── violations.log # Log of script activity
└── timing_parser.py # Python script

## 🔧 Requirements

- Python 3.x  
(No external libraries required — uses `csv` and `logging` from standard library)

---

## 🚀 Usage

```bash
python summarize_report.py