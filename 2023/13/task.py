import sys

patterns = []
with open(sys.argv[1]) as f:
    patterns = [p.split('\n') for p in f.read().strip().split('\n\n')]


def find_reflection(pattern, smudges = 0):
    pivot = len(pattern) - 1

    while pivot != 0:
        up = pattern[pivot - 1]
        down = pattern[pivot]

        if difference(up,down) < 2:
            size = min(len(pattern) - 1 - pivot, pivot)
            to_up = []
            to_down = []

            if pivot < len(pattern)/2:
                to_up = pattern[0:pivot]
                to_down = pattern[pivot:pivot + size][::-1]
            else:
                to_up = pattern[pivot - size - 1:pivot]
                to_down = pattern[pivot:pivot + size][::-1]

            delta = 0
            for i in range(len(to_up)):
                delta += difference(to_up[i], to_down[i])

            if delta == smudges:
                return pivot

        pivot -= 1

    return None


def difference(a, b):
    delta = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            delta += 1
    return delta


def rotate(pattern):
    rows = len(pattern)
    cols = len(pattern[0])

    rotated = [['' for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            rotated[j][rows - 1 - i] = pattern[i][j]

    p = []
    for i in range(len(rotated)):
        p.append(''.join(rotated[i]))

    return p


def solve(pattern, smudges):
    h = find_reflection(pattern, smudges)

    s = 0
    if h is None:
        v = find_reflection(rotate(pattern), smudges)
        if v:
            s += v
    else:
        s += 100 * h

    return s

p1 = 0
p2 = 0
for p in patterns:
    p1 += solve(p, 0)
    p2 += solve(p, 1)

print('PART 1:', p1)
print('PART 2:', p2)
