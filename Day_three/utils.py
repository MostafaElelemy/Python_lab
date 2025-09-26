"""
utils.py
- Input helpers and validation utilities to avoid code duplication.
"""
import os
import re
from datetime import datetime

def prompt_non_empty(prompt_text: str) -> str:
    """Prompt until non-empty (after stripping)."""
    while True:
        s = input(prompt_text).strip()
        if s:
            return s
        print("Error: input cannot be empty. Please try again.")

def prompt_choice(prompt_text: str, valid_choices: list[str]) -> str:
    """Prompt until the user enters one of valid_choices (as strings)."""
    valid = set(valid_choices)
    while True:
        s = input(prompt_text).strip()
        if s in valid:
            return s
        print(f"Error: please enter one of {sorted(valid)}.")

def prompt_positive_int(prompt_text: str) -> int:
    """Prompt for a positive integer."""
    while True:
        s = input(prompt_text).strip()
        if s.isdigit():
            n = int(s)
            if n > 0:
                return n
        print("Error: please enter a positive integer.")

def parse_number_list(prompt_text: str) -> list[float]:
    """
    Prompt for a comma-separated list of numbers, return list[float].
    Accepts integers and floats, with optional whitespace.
    """
    number_re = re.compile(r'^[+-]?(\d+(\.\d+)?|\.\d+)$')
    while True:
        raw = input(prompt_text).strip()
        parts = [p.strip() for p in raw.split(",")]
        if not parts or parts == [""]:
            print("Error: please enter at least one number, comma-separated.")
            continue
        ok = True
        numbers: list[float] = []
        for p in parts:
            if not number_re.match(p):
                ok = False
                break
            try:
                numbers.append(float(p))
            except ValueError:
                ok = False
                break
        if ok:
            return numbers
        print("Error: invalid number list. Example: 3, 4.5, -2, .75")

def parse_str_list(prompt_text: str) -> list[str]:
    """Prompt for a comma-separated list of strings (names)."""
    while True:
        raw = input(prompt_text).strip()
        parts = [p.strip() for p in raw.split(",") if p.strip()]
        if parts:
            return parts
        print("Error: please enter at least one item, comma-separated.")

def parse_price_list(prompt_text: str) -> list[float]:
    """Prompt for a comma-separated list of prices (floats)."""
    while True:
        raw = input(prompt_text).strip()
        parts = [p.strip() for p in raw.split(",")]
        prices: list[float] = []
        ok = True
        for p in parts:
            try:
                prices.append(float(p))
            except ValueError:
                ok = False
                break
        if ok and parts and parts != [""]:
            return prices
        print("Error: please enter valid numeric prices, comma-separated.")

def prompt_existing_directory(prompt_text: str) -> str:
    """Prompt until a valid, existing directory path is entered."""
    while True:
        path = input(prompt_text).strip().strip('"').strip("'")
        if os.path.isdir(path):
            return path
        print("Error: directory does not exist. Please try again.")

def prompt_date(prompt_text: str, fmt: str = "%Y-%m-%d") -> datetime.date:
    """Prompt for a date in a given format, default YYYY-MM-DD."""
    while True:
        s = input(prompt_text).strip()
        try:
            return datetime.strptime(s, fmt).date()
        except ValueError:
            print(f"Error: date must match format {fmt}. Try again.")
