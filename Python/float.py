"""float.py
Shows floating-point division and the limits of decimal precision."""

def main():
    x = int(input("x: "))
    y = int(input("y: "))
    result = x / y
    print(f"{result:.50f}")


if __name__ == "__main__":
    main()
