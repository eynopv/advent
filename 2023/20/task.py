import sys
from typing import List, Tuple
import math
import time

LOW = 0
HIGH = 1

ms = {}
with open(sys.argv[1]) as f:
    data = f.read().splitlines()
    c_dst = {}
    conjuctions = []
    for d in data:
        t, dst = d.split(" -> ")
        dst = dst.split(", ")
        if "%" in t:
            ms[t[1:]] = (t[0], dst, "off")
        elif "&" in t:
            conjuctions.append(t[1:])
            ms[t[1:]] = (t[0], dst, {})
        else:
            ms[t] = (None, dst, None)
    for m, v in ms.items():
        for d in v[1]:
            if d in conjuctions:
                ms[d][2][m] = LOW


pulses = [0, 0]
p2 = 0
rx_deps = {}
for d in ms["cn"][2]:
    rx_deps[d] = 0

start = time.time()
for i in range(1000000000000):
    # source, dst, type
    q: List[Tuple[str, str, int]] = [("button", "broadcaster", LOW)]

    if len([d for d in rx_deps.values() if d > 0]) == len(rx_deps.values()):
        break

    while q:
        src, dst, pulse = q.pop(0)
        pulses[pulse] += 1
        print(src, dst, pulse)

        if dst == "rx" and pulse == LOW:
            p2 = i + 1
            break

        if dst not in ms:
            continue
        # type destinations state
        tp, dsts, state = ms[dst]
        if not tp:
            for d in dsts:
                q.append((dst, d, pulse))
        elif tp == "%":
            if pulse == HIGH:
                continue
            new_state = "on" if state == "off" else "off"
            new_pulse = HIGH if new_state == "on" else LOW
            for d in dsts:
                q.append((dst, d, new_pulse))
            ms[dst] = (tp, dsts, new_state)
        elif tp == "&":
            state[src] = pulse
            ms[dst] = (tp, dsts, state)
            new_pulse = HIGH
            if all(i == 1 for i in state.values()):
                new_pulse = LOW
            for d in ms[dst][1]:
                q.append((dst, d, new_pulse))
            if dst in rx_deps and not rx_deps[dst]:
                if new_pulse == HIGH:
                    rx_deps[dst] = i + 1


print("PART 1:", pulses[0] * pulses[1])
print(rx_deps)
print("PART 2:", math.lcm(*rx_deps.values()))
