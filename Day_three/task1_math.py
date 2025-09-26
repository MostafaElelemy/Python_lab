"""
task1_math.py - Math Automation
- Asks the user for numbers, computes metrics, writes a report file, and prints it.
"""
import math
from pathlib import Path
from decorators import log_time
from utils import parse_number_list

REPORT = "math_report.txt"

@log_time  
def run():
    numbers = parse_number_list("Enter numbers (comma-separated): ")
    lines = []
    header = "value,floor,ceil,sqrt,area_of_circle(pi*r^2)"
    lines.append(header)

    for x in numbers:
        fl = math.floor(x)
        ce = math.ceil(x)
        sqrt_val = math.sqrt(x) if x >= 0 else float("nan")
        area = math.pi * (x ** 2)
        lines.append(f"{x},{fl},{ce},{sqrt_val},{area}")

    Path(REPORT).write_text("\n".join(lines), encoding="utf-8")
    print(f'"{REPORT}" has been created. Content:\n')
    print(Path(REPORT).read_text(encoding="utf-8"))
