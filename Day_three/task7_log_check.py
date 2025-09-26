"""
task7_log_check.py - Decorators Task Validator
- Shows the contents of execution_log.txt, if any.
"""
from pathlib import Path

LOG_FILE = "execution_log.txt"

def run():
    p = Path(LOG_FILE)
    if not p.exists():
        print(f'No log file found at "{LOG_FILE}". Run decorated tasks first (e.g., Task 1 or 2).')
        return
    content = p.read_text(encoding="utf-8")
    if content.strip():
        print("execution_log.txt contents:\n")
        print(content)
    else:
        print(f'"{LOG_FILE}" is empty. Run decorated tasks to populate it.')
