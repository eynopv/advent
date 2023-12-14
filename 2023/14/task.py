import sys
from functools import cache

grid = []
with open(sys.argv[1]) as f:
    grid = [list(line) for line in f.read().splitlines()]


def print_grid(g):
    print('=' * 10)
    for line in g:
        print(''.join(line))
    print('=' * 10)


def rotate(pattern):
    rows = len(pattern)
    cols = len(pattern[0])

    rotated = [['' for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            rotated[j][rows - 1 - i] = pattern[i][j]

    return rotated


def cycle(g):
    cycled = [row[:] for row in g]
    for _ in 'NWES':
        tilted = tilt(cycled)
        rotated = rotate(tilted)
        cycled = rotated
    return cycled


def tilt(g):
    tilted = [row[:] for row in g]
    h = len(g)
    w = len(g[0])
    moved = True

    while moved:
        moved = False
        for row in range(1, h):
            for col in range(0, w):
                cell = tilted[row][col]
                if cell == 'O' and tilted[row - 1][col] == '.':
                    tilted[row - 1][col] = 'O'
                    tilted[row][col] = '.'
                    moved = True
    return tilted

def count(g):
    h = len(g)
    s = 0
    for i in range(h):
        s += g[i].count('O') * (h - i)
    return s

print_grid(grid)

tilted = tilt(grid)
print_grid(tilted)
p1 = count(tilted)
print('PART 1: ', p1)

total_cycles = 1000000000
cache = {}
cycled = [row[:] for row in grid]
result = None
for i in range(total_cycles):
    cycled = cycle(cycled)
    key = ''.join([''.join(row) for row in cycled])
    if key in cache:
        start = cache[key]['idx']
        end = i
        idx = cache[key]['idx'] + (total_cycles - cache[key]['idx']) % (end - start) - 1
        result = [r for r in cache.values() if r['idx'] == idx][0]['state']
        break

    cache[key] = {
            'idx': i,
            'state': cycled
    }

p2 = count(result)
print('PART 2: ', p2)
