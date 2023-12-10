import sys
from loader import load


def main(data):
    first(data)
    second(data)


def first(data):
    total = 0
    for card in data:
        _, lists = card.split(": ")
        winning, numbers = lists.split(" | ")
        winning = [int(n.strip()) for n in winning.split()]
        numbers = [int(n.strip()) for n in numbers.split()]
        points = 0
        for n in numbers:
            if n in winning:
                points = points * 2 if points > 0 else 1
        total += points
    print(f"Points: {total}")


def second(data):
    counts = [1 for _ in range(len(data))]
    for i in range(len(data)):
        card = data[i]
        _, lists = card.split(": ")
        winning, numbers = lists.split(" | ")
        winning = [int(n.strip()) for n in winning.split()]
        numbers = [int(n.strip()) for n in numbers.split()]

        matching = len([n for n in numbers if n in winning])
        for j in range(matching):
            cardcopyidx = i + j + 1
            if cardcopyidx < len(counts):
                counts[cardcopyidx] += counts[i]
    print(f"Cards: {sum(counts)}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Provide data file")
        print("Example: python task.py [data.txt]")
        sys.exit(-1)
    fname = sys.argv[1]
    data = load(fname)
    main(data)
