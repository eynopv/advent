import sys
import math

times = []
distances = []

with open(sys.argv[1]) as f:
    data = f.read().strip().split("\n")
    times = [int(t) for t in data[0].split(":")[1].split()]
    distances = [int(d) for d in data[1].split(":")[1].split()]


def calculate(distance, time):
    sqrtb24ac = math.sqrt(time**2 - 4 * distance)
    minhold = (time - sqrtb24ac) / 2
    maxhold = (time + sqrtb24ac) / 2
    minhold = math.ceil(minhold) if int(minhold) < minhold else int(minhold) + 1
    maxhold = math.floor(maxhold) if int(maxhold) < maxhold else int(maxhold) - 1
    count = maxhold - minhold + 1
    return count


n = 1
for i in range(len(distances)):
    n *= calculate(distances[i], times[i])
print(f"TASK 1: {n}")


time = int("".join([str(t) for t in times]))
distance = int("".join([str(d) for d in distances]))

print(f"TASK 2: {calculate(distance, time)}")
