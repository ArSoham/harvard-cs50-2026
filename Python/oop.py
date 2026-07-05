"""oop.py
A simple object-oriented Python example with a class and method."""


class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")


def main():
    person = Person("Soham")
    person.greet()


if __name__ == "__main__":
    main()
