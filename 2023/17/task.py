import sys
import time

m = []
with open(sys.argv[1]) as f:
    m = [[int(n) for n in list(l)] for l in f.read().splitlines()]


BIG = 9999999999
H = len(m)
W = len(m[0])
DIRS = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def traverse(mmin=1, mmax=3):
    # x, y, loss, previous_direction
    q = [(0, 0, 0, -1)]
    losses = {}
    reached = []

    while q:
        x, y, loss, pd = q.pop(0)

        if x == W - 1 and y == H - 1:
            return [loss]
            reached.append(loss)

        for d in range(len(DIRS)):
            # Not current direction
            if d == pd:
                continue
            # Not opposite direction
            if DIRS[d][0] + DIRS[pd][0] == 0 and DIRS[d][1] + DIRS[pd][1] == 0:
                continue

            increase = 0
            for dst in range(1, mmax + 1):
                nx = x + DIRS[d][0] * dst
                ny = y + DIRS[d][1] * dst

                if nx < 0 or ny < 0 or nx >= W or ny >= H:
                    continue

                increase += m[ny][nx]

                # part 2
                if dst < mmin:
                    continue

                new_loss = loss + increase

                if losses.get((nx, ny, d), BIG) <= new_loss:
                    continue

                losses[(nx, ny, d)] = new_loss
                q.append((nx, ny, new_loss, d))
        q = sorted(q, key=lambda t: t[2])

    return reached


s = time.time()
p1 = min(traverse())
print("PART 1: ", p1)
print("Elapsed", time.time() - s)

s = time.time()
p2 = min(traverse(4, 10))
print("PART 2: ", p2)
print("Elapsed", time.time() - s)
