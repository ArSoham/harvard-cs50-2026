"""dict.py
Demonstrates a phonebook lookup using a list of dictionaries."""

people = [
    {"name": "Kelly", "number": "+1-617-495-1000"},
    {"name": "David", "number": "+1-617-495-1000"},
    {"name": "John", "number": "+1-949-468-2750"},
]


def main():
    name = input("Name: ").strip()
    for person in people:
        if person["name"].lower() == name.lower():
            print(f"Found {person['number']}")
            return
    print("Not found")


if __name__ == "__main__":
    main()
