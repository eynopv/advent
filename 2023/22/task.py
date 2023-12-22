import sys

bricks = []
with open(sys.argv[1]) as f:
    data = [line.split("~") for line in f.read().splitlines()]
    for i in range(len(data)):
        b = data[i]
        p1 = tuple([int(n) for n in b[0].split(",")])
        p2 = [int(n) for n in b[1].split(",")]
        bricks.append((p1, p2, i))
    bricks.sort(key=lambda x: x[0][2])


def fall(bs):
    supports = {i: [] for i in range(len(bs))}
    supported_by = {i: [] for i in range(len(bs))}
    settled = {}

    for b in bs:
        (x1, y1, z1), (x2, y2, z2), i = b
        sups = []

        while z1 > 0 and not sups:
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    for z in range(z1, z2 + 1):
                        if (x, y, z - 1) in settled:
                            sups.append((x, y, z - 1))
            if not sups:
                z1 -= 1
                z2 -= 1

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                for z in range(z1, z2 + 1):
                    settled[(x, y, z)] = i

        for s in set(settled[sup] for sup in sups):
            supports[s].append(i)
            supported_by[i].append(s)

    return supports, supported_by


def get_removable(supports, supported_by):
    removable = set()
    for i in supports:
        is_removable = True
        for j in supports[i]:
            if len(supported_by[j]) == 1:
                is_removable = False
                break
        if is_removable:
            removable.add(i)
    return removable


def get_chain(supports, supported_by, removable):
    chains = {}
    for i in supports:
        if i in removable:
            continue

        q = supports[i].copy()
        chain = set()
        chain.add(i)
        while q:
            f = q.pop()
            if all(j in chain for j in supported_by[f]):
                chain.add(f)
                q += supports[f]
        chains[i] = chain
    return chains


supports, supported_by = fall(bricks)
removable = get_removable(supports, supported_by)
p1 = len(get_removable(supports, supported_by))
print("PART 1:", p1)

chains = get_chain(supports, supported_by, removable)
p2 = sum([len(c) - 1 for c in chains.values()])
print("PART 2:", p2)
