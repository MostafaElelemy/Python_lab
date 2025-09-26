"""
task5_os_manager.py - OS File Manager
- Copies all .txt files into a backup subfolder.
"""
import os
import shutil
from pathlib import Path
from utils import prompt_existing_directory

def run():
    directory = prompt_existing_directory("Enter a valid directory path: ")
    src = Path(directory)
    backup = src / "backup"
    backup.mkdir(exist_ok=True)
    count = 0
    for p in src.glob("*.txt"):
        if p.is_file():
            shutil.copy2(p, backup / p.name)
            count += 1
    print(f"Copied {count} .txt files into {backup}")
