import sys


def process(data):
    return [predict_next(h) for h in data]


def predict_next(h):
    if [n for n in h if n!= 0]:
        return h[-1] + predict_next(get_sequence(h))
    return h[-1]


def get_sequence(h):
    sequence = []
    for i in range(1, len(h)):
        n = h[i] - h[i - 1]
        sequence.append(n)
    return sequence


histories = []

with open(sys.argv[1]) as f:
    data = f.read().strip().split('\n')
    histories = [[int(n) for n in d.split(' ')] for d in data]

print(f'TASK 1: {sum(process(histories))}')
print(f'TASK 2: {sum(process([s[::-1] for s in histories]))}')

