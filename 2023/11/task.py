import sys

space = []

with open(sys.argv[1]) as f:
    space = f.read().splitlines()


def expand():
    emptycols = []
    emptyrows = []

    for r in range(len(space)):
        row = space[r]
        if not "#" in row:
            emptyrows.append(r)

    for c in range(len(space[0])):
        isempty = True
        for r in range(len(space)):
            if space[r][c] == "#":
                isempty = False
        if isempty:
            emptycols.append(c)

    width = len(space[0]) + len(emptycols)
    expanded = [['_' for _ in range(width)] for _ in range(len(space))]


    colinserts = 0
    for c in range(len(space[0])):
        makeinsert = c in emptycols
        ec = c + colinserts
        for r in range(len(space)):
            expanded[r][ec] = space[r][c]
            if makeinsert:
                expanded[r][ec + 1] = "c"
        if makeinsert:
            colinserts += 1

    rowinserts = 0
    for r in range(len(space[0])):
        makeinsert = r in emptyrows
        if makeinsert:
            expanded = (
                expanded[0 : r + rowinserts]
                + [["r" for _ in range(len(expanded[0]))]]
                + expanded[r + rowinserts :]
            )
            rowinserts += 1
    return expanded


expanded = expand()

for e in expanded:
    print(e)

galaxies = []
for row in range(len(expanded)):
    for col in range(len(expanded[0])):
        if expanded[row][col] == '#':
            galaxies.append((row, col))

distances = []

while galaxies:
    g = galaxies.pop()
    for other in galaxies:
        distances.append(abs(other[0] - g[0]) + abs(other[1] - g[1]))

print('PART 1:', sum(distances))

offset = 1000000 - 2
roffset = 0

for row in range(len(expanded)):
    if 'r' in expanded[row]:
        roffset += offset
        continue

    coffset = 0
    for col in range(len(expanded[0])):
        if expanded[row][col] == 'c':
            coffset += offset
        if expanded[row][col] == '#':
            galaxies.append((row + roffset, col + coffset))

distances = []

while galaxies:
    g = galaxies.pop()
    for other in galaxies:
        distances.append(abs(other[0] - g[0]) + abs(other[1] - g[1]))

print('PART 2:', sum(distances))
