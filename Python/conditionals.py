"""conditionals.py
Basic conditional examples using user input.
"""

try:
    from cs50 import get_string
except ImportError:
    get_string = input


def agree_with_cs50():
    """Ask the user for agreement using CS50 get_string if available."""
    answer = get_string("Do you agree? ").strip()
    if answer in ("Y", "y"):
        print("Agreed.")
    else:
        print("Not agreed.")


def agree_with_input():
    """Ask the user for agreement using standard Python input."""
    answer = input("Do you agree? ").strip().lower()
    if answer in ["y", "yes"]:
        print("Agreed.")
    else:
        print("Not agreed.")


if __name__ == "__main__":
    agree_with_cs50()
    agree_with_input()
