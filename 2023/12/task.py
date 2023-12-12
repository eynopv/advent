import sys
from functools import cache
import time

data = []

with open(sys.argv[1]) as f:
    data = f.read().splitlines()


@cache
def count_options(s, validators, current_group):
    # valid option
    if not s:
        if not current_group and not validators:
            return 1
        if len(validators) == 1 and current_group == validators[0]:
            return 1
        return 0

    # invalid option
    if current_group and not validators:
        return 0
    if current_group and current_group > validators[0]:
        return 0
    if current_group and s[0] == "." and current_group != validators[0]:
        return 0
    if s.count("#") + s.count("?") + current_group < sum(validators):
        return 0

    if s[0] == "?":
        c = 0
        c += count_options("#" + s[1:], validators, current_group)
        c += count_options("." + s[1:], validators, current_group)
        return c

    if s[0] == "#":
        if current_group:
            return count_options(s[1:], validators, current_group + 1)
        return count_options(s[1:], validators, 1)

    if s[0] == ".":
        if current_group and current_group == validators[0]:
            return count_options(s[1:], validators[1:], 0)
        return count_options(s[1:], validators, 0)

    return 0


p1 = 0
p2 = 0
start = time.time()
for d in [d.split(" ") for d in data]:
    springs = d[0]
    validators = tuple([int(v) for v in d[1].split(",")])
    p1 += count_options(springs, validators, 0)
    p2 += count_options("?".join([springs] * 5), validators * 5, 0)
end = time.time()

print("PART 1:", p1)
print("PART 2:", p2)
print("Elapsed:", end - start)
