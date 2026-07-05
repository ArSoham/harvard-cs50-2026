"""hello.py
Reads a user's name and prints several greeting styles."""

def main():
    name = input("What's your name? ").strip()
    print("Your name is " + name)
    print(f"Hello, {name}")
    print("hello, world", end="!!!")


if __name__ == "__main__":
    main()
