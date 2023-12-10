import sys
from typing import List, Tuple

sys.setrecursionlimit(100000)

maze = []

with open(sys.argv[1]) as f:
    maze = f.read().splitlines()


x, y = 0, 0
for row in range(len(maze)):
    for col in range(len(maze[row])):
        if maze[row][col] == "S":
            x = col
            y = row
            break
    if x or y:
        break


def find_routes(route):
    lx, ly = route[-1]
    if len(route) > 1 and maze[ly][lx] == "S":
        print("loop", route)
        return [route]

    adjacent = [(lx, ly - 1), (lx, ly + 1), (lx - 1, ly), (lx + 1, ly)]

    routes = []
    for n in adjacent:
        nx, ny = n[0], n[1]
        node = get_node(n[0], n[1])

        if not node or node == ".":
            continue

        if node != "S" and (nx, ny) in route:
            continue

        if can_connect(maze[ly][lx], maze[ny][nx], nx - lx, ny - ly):
            routes += find_routes(route + [(nx, ny)])

    return routes


def get_node(x: int, y: int) -> str | None:
    if y < 0 or y >= len(maze):
        return None
    if x < 0 or x >= len(maze[0]):
        return None
    return maze[y][x]


connections = {
    "|": ["north", "south"],
    "-": ["east", "west"],
    "L": ["north", "east"],
    "J": ["north", "west"],
    "7": ["south", "west"],
    "F": ["south", "east"],
    ".": [],
    "S": ["north", "east", "south", "west"],
}


def can_connect(a: str, b: str, xd: int, yd: int) -> bool:
    dfrom = ""
    dto = ""
    if xd > 0:
        dfrom = "west"
        dto = "east"
    elif xd < 0:
        dfrom = "east"
        dto = "west"
    elif yd > 0:
        dfrom = "north"
        dto = "south"
    else:
        dfrom = "south"
        dto = "north"
    return dto in connections[a] and dfrom in connections[b]


longest = max(r for r in find_routes([(x, y)]))
print(f"TASK 1: {(len(longest) - 1)/2}")

ct = 0
grid = [["_" for _ in range(len(maze[0]))] for _ in range(len(maze))]

for row in range(len(maze)):
    inside = False
    for col in range(len(maze[0])):
        if (col, row) in longest:
            grid[row][col] = "x"
            if maze[row][col] in ["|", "J", "L"]:
                inside = not inside
            elif maze[row][col] == "S":
                fp = longest[1]
                first = maze[fp[1]][fp[0]]
                lp = longest[-1]
                last = maze[lp[1]][lp[0]]
                for i in ["|", "L", "J"]:
                    fconnect = can_connect(i, first, fp[0] - col, fp[1] - row)
                    lconnect = can_connect(last, i, col - lp[0], row - fp[1])
                    if fconnect and lconnect:
                        inside = not inside

        elif inside:
            ct += 1
            grid[row][col] = "O"

for line in grid:
    print(line)
print("TASK 2", ct)
