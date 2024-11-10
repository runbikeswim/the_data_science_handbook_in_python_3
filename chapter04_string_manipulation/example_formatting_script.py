"""
runs functions for typical formatting tasks

change directory to chapter04_string_manipulation and then execute  
    python -m example_formatting_script
"""

import pandas as pd

def get_first_last_name(text:str) -> tuple[str, str]:
    """
    extracts the first and last name from a given text
    """

    PARTS_TO_BE_SKIPPED = ["mr ", "ms", "mrs", "dr", "jr", "sir "]

    parts = text.lower().replace(".", "").strip().split()

    parts = (
            [
                p.capitalize() for p in parts
                    if p not in PARTS_TO_BE_SKIPPED
            ]
        )

    match len(parts):
        case 0:
            raise ValueError("Name %s is formatted wrong " % text)
        case 1:
            first, last = "", parts[0]
        case _:
            first, last = " ".join(parts[0:-1]), parts[-1]

    return first, last

def format_age(s):

    chars = list(s) # list of characters
    digit_chars = [c for c in chars if c.isdigit()]
    return int("".join(digit_chars))

def format_date(s):

    MONTH_MAP = {
            "jan": "01", "feb": "02", "may": "03"
        }

    s = s.strip().lower().replace(",", "")
    m, d, y = s.split()
    if len(y) == 2: 
        y = "19" + y

    if len(d) == 1: 
        d = "0" + d

    return y + "-" + MONTH_MAP[m[:3]] + "-" + d

df = pd.read_csv("file.tsv", sep="|")

df["First Name"] = (
        df["Name"]
        .map(
            lambda s: get_first_last_name(s)[0]
        )
    )

df["Last Name"] = (
        df["Name"]
        .map(
            lambda s: get_first_last_name(s)[1]
        )
    )

df["Age"] = df["Age"].map(format_age)

df["Birthdate"] = (
        pd.to_datetime(df["Birthdate"], format="mixed")
    )

print(df)
