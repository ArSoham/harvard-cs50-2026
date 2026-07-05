"""exception.py
Illustrates exception handling and simple list search examples."""


def integer_input():
    try:
        n = int(input("Input: "))
        print("Integer.")
    except ValueError:
        print("Not integer.")


def search_names():
    names = ["Kelly", "David", "John"]
    name = input("Name: ").strip()
    if name in names:
        print("Found")
    else:
        print("Not found")


def search_names_case_insensitive():
    names = ["Kelly", "David", "John"]
    user_name = input("Name: ").strip().lower()
    if user_name in [n.lower() for n in names]:
        print("Name found")
    else:
        print("Not found")


if __name__ == "__main__":
    integer_input()
    search_names()
    search_names_case_insensitive()
