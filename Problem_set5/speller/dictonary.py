"""dictonary.py
A simple Python dictionary helper used for CS50-like spell-checking practice.
"""

words = set()


def check(word):
    """Return True if word is in the dictionary, else False."""
    return word.lower() in words


def load(dictionary):
    """Load dictionary words into memory and return True if successful."""
    with open(dictionary, "r", encoding="utf-8") as file:
        for line in file:
            words.add(line.strip().lower())
    return True


def size():
    """Return number of words loaded in the dictionary."""
    return len(words)


def unload():
    """Clear the loaded dictionary from memory."""
    words.clear()
    return True
