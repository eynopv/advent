import sys
from typing import List, Tuple

# Based on Pick's theoreme
# https://en.wikipedia.org/wiki/Pick%27s_theorem

plan = []
with open(sys.argv[1]) as f:
    plan = [line.split() for line in f.read().splitlines()]


def solve(moves):
    holes: List[Tuple[int, int]] = [(0, 0)]
    boundary = 0

    for m in moves:
        x, y = holes[-1]

        if m[0] == "R":
            x += m[1]
        elif m[0] == "L":
            x -= m[1]
        elif m[0] == "D":
            y += m[1]
        elif m[0] == "U":
            y -= m[1]
        holes.append((x, y))
        boundary += m[1]

    area = calculate_polygon_area(holes)
    interior = calculate_interior_points(area, boundary)
    return interior + boundary


def calculate_polygon_area(polygon):
    area = 0.0
    for i in range(len(polygon)):
        j = (i + 1) % len(polygon)
        x1, y1 = polygon[i]
        x2, y2 = polygon[j]
        area += x1 * y2
        area -= x2 * y1
    return abs(area) / 2.0


def calculate_interior_points(area, perimeter):
    return int(area - 0.5 * perimeter + 1)


p1 = solve([(p[0], int(p[1])) for p in plan])
print("PART 1:", p1)

DIRS = ["R", "D", "L", "U"]
p2 = solve([(DIRS[int(p[2][-2:-1])], int(p[2][2:-2], 16)) for p in plan])
print("PART 2:", p2)
