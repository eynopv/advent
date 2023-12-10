import sys
from functools import cmp_to_key

STRENGTH = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
STRENGTH_2 = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
hands = []

with open(sys.argv[1]) as f:
    hands = [h.split() for h in f.read().strip().split("\n")]


def compare_counts(a, b):
    delta = a[1] - b[1]
    if delta != 0:
        return delta
    return STRENGTH.index(a[0]) - STRENGTH.index(b[0])


def compare_counts_2(a, b):
    delta = a[1] - b[1]
    if delta != 0:
        return delta
    return STRENGTH_2.index(a[0]) - STRENGTH_2.index(b[0])


def evaluate(hands):
    evaluated = []
    for i in range(len(hands)):
        h = hands[i]
        cards, score = h[0], int(h[1])
        counts = {}
        for c in cards:
            counts[c] = counts[c] + 1 if c in counts else 1

        ordered_counts = sorted(
            counts.items(), key=cmp_to_key(compare_counts), reverse=True
        )

        rank = calculate_rank(ordered_counts)

        js = counts.get("J", 0)
        counts2 = sorted(
            [c for c in ordered_counts.copy() if c[0] != "J"],
            key=cmp_to_key(compare_counts_2),
            reverse=True,
        )
        if not counts2:
            counts2 = [("J", 0)]

        print(counts2)
        counts2[0] = (counts2[0][0], counts2[0][1] + js)
        rank2 = calculate_rank(counts2)

        evaluated.append((cards, score, rank, ordered_counts, rank2))

    return evaluated


def calculate_rank(counts):
    rank = 1
    for card, count in counts:
        if count == 5:
            rank += 54
        elif count == 4:
            rank += 18
        elif count == 3:
            rank += 6
        elif count == 2:
            rank += 2
    return rank


def compare_hands(a, b):
    delta = a[2] - b[2]
    if delta != 0:
        return delta

    for i in range(len(a[0])):
        acard = STRENGTH.index(a[0][i])
        bcard = STRENGTH.index(b[0][i])
        delta = acard - bcard
        if delta != 0:
            return delta


def compare_hands_2(a, b):
    delta = a[4] - b[4]
    if delta != 0:
        return delta

    for i in range(len(a[0])):
        acard = STRENGTH_2.index(a[0][i])
        bcard = STRENGTH_2.index(b[0][i])
        delta = acard - bcard
        if delta != 0:
            return delta

    return 0


ordered = sorted(evaluate(hands), key=cmp_to_key(compare_hands))
score = 0
for i in range(1, len(ordered) + 1):
    print(ordered[i - 1])
    score += i * ordered[i - 1][1]
print("TASK 1:", score)

ordered = sorted(evaluate(hands), key=cmp_to_key(compare_hands_2))
score = 0
for i in range(1, len(ordered) + 1):
    print(ordered[i - 1])
    score += i * ordered[i - 1][1]
print("TASK 2:", score)
