"""
task2_regex.py - Regex Log Cleaner
- Generates an access.log with mixed lines.
- Extracts valid emails into valid_emails.txt and prints the count of UNIQUE emails.
"""
import random
import re
from pathlib import Path
from decorators import log_time

LOG_FILE = "access.log"
OUT_FILE = "valid_emails.txt"

EMAIL_RE = re.compile(r"""
    (?<![A-Za-z0-9._%+-])           
    [A-Za-z0-9._%+-]+
    @
    [A-Za-z0-9.-]+\.[A-Za-z]{2,}
    (?![A-Za-z0-9._%+-])            
""", re.X)

fake_domains = ["example.com", "mail.net", "test.org", "company.io"]
invalid_chunks = ["@@", "not-an-email", "foo#bar", "user@bad_domain", "nope", "12345"]

def _random_email():
    user = "".join(random.choices("abcdefghijklmnopqrstuvwxyz0123456789._", k=random.randint(5,12)))
    domain = random.choice(fake_domains)
    return f"{user}@{domain}"

def _random_line():
    if random.random() < 0.6:  
        return f"INFO user={_random_email()} status=200"
    else:
        return f"INFO blob={random.choice(invalid_chunks)} ref={random.randint(1000,9999)}"

@log_time  
def run():
    
    lines = [_random_line() for _ in range(10)]
    Path(LOG_FILE).write_text("\n".join(lines), encoding="utf-8")
    print(f'Generated "{LOG_FILE}".')
   
    text = "\n".join(lines)
    emails = set(m.group(0) for m in EMAIL_RE.finditer(text))
    Path(OUT_FILE).write_text("\n".join(sorted(emails)), encoding="utf-8")
    print(f'Found {len(emails)} unique valid emails. Saved to "{OUT_FILE}".')
