"""
task3_datetime.py - Datetime Reminder Script
"""
from datetime import date
from pathlib import Path
from utils import prompt_date

REM_FILE = "reminders.txt"

def run():
    target = prompt_date("Enter a date (YYYY-MM-DD): ")
    today = date.today()
    delta = (target - today).days
    if delta < 0:
        print("This date has already passed.")
        return
    line = f"{target.isoformat()} -> {delta} days left"
    with open(REM_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"Saved: {line}")
