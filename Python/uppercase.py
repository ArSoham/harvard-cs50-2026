"""uppercase.py
Demonstrates converting text to uppercase character by character and using str.upper()."""

def main():
    before = input("Before: ")
    print("After: ", end="")
    for c in before:
        print(c.upper(), end="")
    print()

    after = before.upper()
    print(f"After: {after}")


if __name__ == "__main__":
    main()
