"""phonebook1.py
Appends a contact to phonebook.csv using a CSV dictionary writer."""

import csv


def main():
    name = input("Name: ").strip()
    number = input("Number: ").strip()

    with open("phonebook.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "number"])
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow({"name": name, "number": number})

    print("Contact saved.")


if __name__ == "__main__":
    main()
