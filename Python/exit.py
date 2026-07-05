"""exit.py
Demonstrates command-line arguments and explicit process exit codes."""

import sys


def main():
    if len(sys.argv) != 2:
        print("Missing command line argument")
        sys.exit(1)

    print(f"hello, {sys.argv[1]}")
    sys.exit(0)


if __name__ == "__main__":
    main()
