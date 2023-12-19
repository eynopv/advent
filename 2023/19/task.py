import sys

workflows = {}
parts = []
first = "in"
with open(sys.argv[1]) as f:
    wf, ps = f.read().strip().split("\n\n")
    wf = wf.splitlines()
    ps = ps.splitlines()

    for w in wf:
        name, rules = w.split("{")
        rules = rules[:-1]
        workflows[name] = rules.strip().split(",")

    for p in ps:
        conditions = p[1:-1].split(",")
        d = {}
        for c in conditions:
            name, value = c.split("=")
            d[name] = int(value)
        parts.append(d)


accepted = []
for p in parts:
    current_flow = first
    f = workflows[current_flow]
    while f:
        for rule in f:
            if len(rule) < 6:
                if rule == "A":
                    accepted.append(p)
                    f = None
                elif rule == "R":
                    f = None
                else:
                    f = workflows[rule]
                break

            condition, result = rule.split(":")
            sign = condition[1]
            name, value = condition.split(sign)

            yay = False
            if sign == ">":
                yay = p[name] > int(value)
            elif sign == "<":
                yay = p[name] < int(value)

            if yay:
                if result == "A":
                    accepted.append(p)
                    f = None
                elif result == "R":
                    f = None
                else:
                    f = workflows[result]
                break

p1 = 0
for a in accepted:
    p1 += sum(a.values())
print("PART 1:", p1)


def update_range(name, sign, value, rng):
    idx = "xmas".index(name)
    updated_ranges = []

    for r in rng:
        r = list(r)
        low, high = r[idx]

        if sign == ">":
            low = max(low, value + 1)
        else:
            high = min(high, value - 1)

        if low <= high:
            r[idx] = (low, high)
            updated_ranges.append(tuple(r))

    return updated_ranges


def get_combinations_count(flow):
    def inner_ranges(rules):
        rule = rules[0]
        if rule == "R":
            return []
        if rule == "A":
            return [((1, 4000),) * 4]
        if ":" not in rule:
            return inner_ranges(workflows[rule])

        condition, result = rule.split(":")
        sign = condition[1]
        name = condition[0]
        value = int(condition[2:])
        value_inverted = value + 1 if sign == ">" else value - 1
        sign_inverted = "<" if sign == ">" else ">"

        if_true = update_range(name, sign, value, inner_ranges([result]))
        if_false = update_range(
            name, sign_inverted, value_inverted, inner_ranges(rules[1:])
        )

        return if_true + if_false

    ranges_outer = inner_ranges(workflows[flow])
    combinations = 0

    for rng in ranges_outer:
        v = 1
        for low, high in rng:
            v *= high - low + 1
        combinations += v

    return combinations


p2 = get_combinations_count("in")
print("PART 2:", p2)
