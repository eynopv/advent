import sys
import math

directions = ''
nodes = {}

with open(sys.argv[1]) as f:
    data = [l for l in f.read().strip().split('\n') if l]
    directions, pre_nodes = data[0], data[1:]
    pre_nodes = [n.split(' = ') for n in pre_nodes]
    
    for name, children in pre_nodes:
        children = children[1:-1]
        nodes[name] = tuple(children.split(', '))

current_node = 'AAA'
last_node = 'ZZZ'
current_direction = 0
steps = 0

if current_node in nodes:
    while current_node != last_node:
        if current_direction >= len(directions):
            current_direction = 0
        idx = 0 if directions[current_direction] == 'L' else 1

        current_node = nodes[current_node][idx]

        steps += 1
        current_direction += 1

    print(f'TASK 1: {steps}')



current_nodes = [name for name in nodes if name[-1] == 'A']
current_direction = 0
nsteps = []

for cr in current_nodes:
    steps = 0
    current_node = cr
    while True:
        steps += 1
        if current_direction >= len(directions):
            current_direction = 0
        idx = 0 if directions[current_direction] == 'L' else 1

        current_node = nodes[current_node][idx]
        current_direction += 1
        if current_node[-1] == 'Z':
            break
    nsteps.append(steps)

print(nsteps)
print(f'TASK 2: {math.lcm(*nsteps)}')


