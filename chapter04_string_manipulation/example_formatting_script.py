"""
runs functions for typical formatting tasks

change directory to chapter04_string_manipulation and then execute  
    python -m example_formatting_script
"""

import pandas as pd

FILENAME = "file.tsv"
COLUMNS_SEPARATOR = "|"
NAME_PARTS_TO_BE_SKIPPED = ["mr ", "ms", "mrs", "dr", "jr", "sr", "sir"]

def get_first_last_name(name:str) -> tuple[str, str]:
    """
    extracts the first and last name from a given string containing all parts
    """

    name_parts = name.lower().replace(".", "").strip().split()

    filtered_and_capitalized_parts = (
            [
                p.capitalize() for p in name_parts
                    if p not in NAME_PARTS_TO_BE_SKIPPED
            ]
        )

    match len(filtered_and_capitalized_parts):

        case 0:
            raise ValueError(f"Name '{name}' is formatted wrong")

        case 1:
            first_name =  ""
            last_name = filtered_and_capitalized_parts[0]

        case _:
            first_name = " ".join(filtered_and_capitalized_parts[0:-1])
            last_name = filtered_and_capitalized_parts[-1]

    return first_name, last_name


def extract_number(age_string: str) -> int|float:
    """
    converts a string containing numbers into an integer
    """

    try:
        digit_chars = [c for c in age_string if c.isdigit()]

        return int("".join(digit_chars))
    
    except TypeError:
        return float("nan")

print(f"reading data from file '{FILENAME}' ...")
people = pd.read_csv(FILENAME, sep = COLUMNS_SEPARATOR)

print("extracting first and last name ...")
first_name_last_name = (
        people["Name"]
        .map(
            get_first_last_name
        )
    )

people["First Names"] = first_name_last_name.map(lambda t: t[0])
people["Last Name"] = first_name_last_name.map(lambda t: t[1])

people["Age (converted)"] = people["Age"].map(extract_number)

print("converting birthdate ...")
people["Birthdate (converted)"] = (
        pd.to_datetime(people["Birthdate"], format="mixed")
    )

people.info()

print(people)
