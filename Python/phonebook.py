"""phonebook.py
Searches a small phonebook using a list of dictionaries."""

phonebook = [
    {"name": "Kelly", "number": "+1-617-495-1000"},
    {"name": "David", "number": "+1-617-495-1000"},
    {"name": "John", "number": "+1-949-468-2750"},
]


def main():
    name = input("Name: ").strip()

    for entry in phonebook:
        if entry["name"].lower() == name.lower():
            print(f"Found {entry['number']}")
            return

    print("Not found")


if __name__ == "__main__":
    main()
