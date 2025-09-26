"""
decorators.py
- Contains reusable decorators.
"""
from functools import wraps
from time import perf_counter
from datetime import datetime

LOG_FILE = "execution_log.txt"

def log_time(func):
    """
    Decorator that measures execution time of a function and logs it.
    Writes lines to execution_log.txt in the format:
    [YYYY-MM-DD HH:MM:SS] func_name -> X.YYYYY seconds
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            elapsed = perf_counter() - start
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(LOG_FILE, "a", encoding="utf-8") as f:
                f.write(f"[{timestamp}] {func.__name__} -> {elapsed:.6f} seconds\n")
    return wrapper
