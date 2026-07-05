"""loops.py
Demonstrates for loops, while loops, and function calls in Python."""


def for_loop_example(count):
    for _ in range(count):
        print("meow")


def while_loop_example():
    j = 0
    while j <= 3:
        print("While")
        j += 1


def list_loop_example():
    for item in [0, 1, 2]:
        print("sam")


def main():
    for_loop_example(3)
    while_loop_example()
    list_loop_example()
    for_loop_example(2)


if __name__ == "__main__":
    main()
