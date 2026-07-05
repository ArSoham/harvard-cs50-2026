"""scores.py
Collects several scores and prints their average."""

def main():
    scores = []
    for i in range(3):
        score = int(input("Score: "))
        scores.append(score)

    average = sum(scores) / len(scores)
    print(f"Average: {average}")


if __name__ == "__main__":
    main()
