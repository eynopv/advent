from loader import load


def main(data):
    parts = []
    gears = {}

    for y in range(len(data)):
        current = ""
        ispart = False
        adjacentgears = set()

        for x in range(len(data[y])):
            positions = getadjacentcoordinates(y, x)
            if data[y][x].isdigit():
                current += data[y][x]
                for p in positions:
                    if issymbolat(data, p[0], p[1]):
                        ispart = True
                        break
                for p in positions:
                    if isvalidposition(data, p[0], p[1]) and data[p[0]][p[1]] == "*":
                        adjacentgears.add(f"{p[0]}-{p[1]}")
                print(current, ispart)
            else:
                if current and ispart:
                    parts.append(int(current))
                if current and len(adjacentgears):
                    for g in adjacentgears:
                        gears[g] = (
                            [int(current)]
                            if g not in gears
                            else gears[g] + [int(current)]
                        )
                current = ""
                ispart = False
                adjacentgears = set()
        if current and ispart:
            parts.append(int(current))
        if current and len(adjacentgears):
            for g in adjacentgears:
                gears[g] = (
                    [int(current)] if g not in gears else gears[g] + [int(current)]
                )

    print(parts)
    print("SUM", sum(parts))
    print(gears)

    gearsum = 0
    for g in gears.values():
        if len(g) == 2:
            gearsum += g[0] * g[1]
    print(gearsum)


def getadjacentcoordinates(y, x):
    return [
        (y, x - 1),
        (y, x + 1),
        (y - 1, x),
        (y + 1, x),
        (y - 1, x - 1),
        (y + 1, x - 1),
        (y - 1, x + 1),
        (y + 1, x + 1),
    ]


def hasadjacentsymbol(data, y, x):
    return (
        issymbolat(data, y, x - 1)
        or issymbolat(data, y, x + 1)  # left
        or issymbolat(data, y - 1, x)  # right
        or issymbolat(data, y + 1, x)  # up
        or issymbolat(data, y - 1, x - 1)  # down
        or issymbolat(data, y + 1, x - 1)  # up left
        or issymbolat(data, y - 1, x + 1)  # down left
        or issymbolat(data, y + 1, x + 1)  # up right
    )  # down right


def issymbolat(data, y, x):
    if isvalidposition(data, y, x):
        return not data[y][x].isdigit() and data[y][x] != "."
    return False


def isvalidposition(data, y, x):
    if y < 0 or x < 0:
        return False
    return y < len(data) and x < len(data[y])


if __name__ == "__main__":
    data = load("./data.txt")
    main(data)
