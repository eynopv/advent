import sys

grid = []
with open(sys.argv[1]) as f:
    grid = f.read().splitlines()


def find_start():
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "S":
                return (x, y)


def is_valid(x, y):
    return x >= 0 and y >= 0 and x < len(grid[0]) and y < len(grid)


H = len(grid)
W = len(grid[0])

steps = 26501365  # 64
q = set()
q.add(find_start())
# up, right, down, left
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
p1 = 0
for i in range(1, H * 3):
    if i == 65:
        p1 = len(q)

    next_step = set()

    for plot in q:
        for d in directions:
            xx = plot[0] + d[0]
            yy = plot[1] + d[1]
            if grid[yy % H][xx % W] != "#":
                next_step.add((xx, yy))
    q = next_step

    if i % H == steps % H:
        print(i, len(q), i // H)

print("PART 1: ", p1)

d = steps // H
a0 = 3882
a1 = 34441
a2 = 95442
b0 = a0
b1 = a1 - a0
b2 = a2 - a1
p2 = b0 + b1 * d + (d * (d - 1) // 2) * (b2 - b1)
print("PART 2:", p2)
