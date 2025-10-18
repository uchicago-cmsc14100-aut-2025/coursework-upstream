"""
CMSC 14100
Autumn 2025

Module to load texts.
"""
import sys

def load_text():
    """
    Try to load the provided password file.
    """
    filename = "linkedin_anon.txt"
    try: 
        with open(filename) as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError as e:
        print(f"Cannot open text file: {filename}", file=sys.stderr)
        sys.exit(1)
