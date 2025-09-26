"""
task6_random_data.py - Random Data Generator
"""
import csv
import random
from statistics import mean
from utils import prompt_positive_int

OUT_FILE = "random_numbers.csv"

def run():
    n = prompt_positive_int("How many random integers to generate? ")
    values = [random.randint(0, 100) for _ in range(n)]
    with open(OUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["index", "value"])
        for i, v in enumerate(values, start=1):
            writer.writerow([i, v])
    avg = mean(values) if values else 0.0
    print(f"Generated {n} numbers. Average = {avg:.2f}. Saved to {OUT_FILE}.")
