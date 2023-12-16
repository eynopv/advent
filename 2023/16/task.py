import sys
from functools import cache
from typing import List, Tuple
import time

grid = []
with open(sys.argv[1]) as f:
    grid = f.read().splitlines()


def make_move(x, y, d):
    if d == "r":
        x += 1
    elif d == "l":
        x -= 1
    elif d == "u":
        y -= 1
    elif d == "d":
        y += 1
    return (x, y, d)


def is_invalid(x, y):
    return x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid)


@cache
def process_move(move):
    x, y, d = move
    new_moves = []

    if grid[y][x] == ".":
        new_moves.append(make_move(x, y, d))

    if grid[y][x] == "|":
        if d in "lr":
            new_moves.append(make_move(x, y, "u"))
            new_moves.append(make_move(x, y, "d"))
        else:
            new_moves.append(make_move(x, y, d))

    if grid[y][x] == "-":
        if d in "ud":
            new_moves.append(make_move(x, y, "l"))
            new_moves.append(make_move(x, y, "r"))
        else:
            new_moves.append(make_move(x, y, d))

    if grid[y][x] == "/":
        if d == "u":
            new_moves.append(make_move(x, y, "r"))
        elif d == "d":
            new_moves.append(make_move(x, y, "l"))
        elif d == "l":
            new_moves.append(make_move(x, y, "d"))
        elif d == "r":
            new_moves.append(make_move(x, y, "u"))

    if grid[y][x] == "\\":
        if d == "u":
            new_moves.append(make_move(x, y, "l"))
        elif d == "d":
            new_moves.append(make_move(x, y, "r"))
        elif d == "l":
            new_moves.append(make_move(x, y, "u"))
        elif d == "r":
            new_moves.append(make_move(x, y, "d"))

    return tuple(new_moves)


def process(move):
    visited = set()
    known_moves = []
    q = [move]

    while q:
        x, y, d = q.pop(0)
        if is_invalid(x, y) or (x, y, d) in known_moves:
            continue
        known_moves.append((x, y, d))
        visited.add((x, y))

        q.extend(process_move((x, y, d)))

    return len(visited)


s = time.time()
print("PART 1:", process((0, 0, "r")))
elapsed = time.time() - s
print("Elapsed seconds:", elapsed)


starts = []
for row in range(len(grid)):
    starts.append((0, row, "r"))
    starts.append((len(grid[0]) - 1, row, "l"))
for col in range(len(grid[0])):
    starts.append((col, 0, "d"))
    starts.append((col, len(grid) - 1, "u"))

print("Part 2 should take", elapsed * len(starts), "seconds maximum")

s = time.time()
print("PART 2:", max([process(m) for m in starts]))
print("Elapsed seconds:", time.time() - s)
