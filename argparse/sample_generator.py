import random

sample_words = [
    "VLSI", "Python", "automation", "script", "error", "signal", "clock", "module",
    "EDA", "timing", "setup", "violation", "logic", "synthesis", "netlist", "report"
]

with open("sample_test_file.txt", "w") as f:
    for _ in range(30):  # 30 lines
        line = " ".join(random.choices(sample_words, k=random.randint(5, 10)))
        f.write(line + "\n")

print("sample_test_file.txt created.")
