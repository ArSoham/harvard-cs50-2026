"""sys.py
Reads a command-line argument and prints a greeting."""

from sys import argv


def main():
    if len(argv) == 2:
        print(f"hello, {argv[1]}")
    else:
        print("hello, world")


if __name__ == "__main__":
    main()
