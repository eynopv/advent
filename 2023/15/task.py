import sys

data = []
with open(sys.argv[1]) as f:
    data = f.read().strip().split(",")

print(data)


def make_hash(s):
    value = 0
    for c in s:
        value += ord(c)
        value *= 17
        value %= 256
    return value


p1 = 0
for s in data:
    p1 += make_hash(s)

print("PART 1:", p1)


lenses = {}
boxes = [[] for _ in range(256)]


def get_lens_position(box, label):
    for i in range(len(box)):
        if box[i][0] == label:
            return i
    return -1


def add_lens(label, focal):
    if label not in lenses:
        lenses[label] = make_hash(label)
    box = lenses[label]
    lens_pos = get_lens_position(boxes[box], label)
    print("Adding", label, focal, "to box", box)
    if lens_pos < 0:
        boxes[box].append((label, focal))
    else:
        boxes[box][lens_pos] = (label, focal)


def remove_lens(label):
    if label not in lenses:
        return
    lens_pos = get_lens_position(boxes[lenses[label]], label)
    print("Removing", label, "from box", lenses[label])
    if lens_pos >= 0:
        boxes[lenses[label]] = (
            boxes[lenses[label]][0:lens_pos] + boxes[lenses[label]][lens_pos + 1 :]
        )


for s in data:
    if "=" in s:
        add_lens(s[:-2], int(s[-1]))
    else:
        remove_lens(s[:-1])

    for box in boxes[:5]:
        print(box)
    print("-" * 5)


p2 = 0
for i in range(len(boxes)):
    for j in range(len(boxes[i])):
        a = i + 1
        b = j + 1
        c = boxes[i][j][1]
        print(a, b, c, a * b * c)
        p2 += a * b * c
print("PART 2:", p2)
