"""
task4_products.py - Product Data Transformer
- Demonstrates lambda, map, filter, zip.
"""
import json
from utils import parse_str_list, parse_price_list

OUT_FILE = "products.json"

def run():
    names = parse_str_list("Enter product names (comma-separated): ")
    prices = parse_price_list("Enter product prices (comma-separated): ")

    while len(names) != len(prices):
        print(f"Error: you entered {len(names)} names but {len(prices)} prices. Please re-enter both.")
        names = parse_str_list("Enter product names (comma-separated): ")
        prices = parse_price_list("Enter product prices (comma-separated): ")

    paired = list(zip(names, prices))

    filtered = list(filter(lambda p: p[1] > 0, paired))

    transformed = list(map(lambda p: {"product": p[0], "price": p[1], "discounted": p[1] * 0.9}, filtered))

    with open(OUT_FILE, "w", encoding="utf-8") as f:
        json.dump(transformed, f, ensure_ascii=False, indent=2)

    print(f'Saved {len(transformed)} items to "{OUT_FILE}". Preview of first 5:')
    for item in transformed[:5]:
        print(item)
