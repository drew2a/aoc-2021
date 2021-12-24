import sys
from collections import Counter
from math import prod
from pathlib import Path
from statistics import mean

inputs = Path(sys.argv[1]).read_text().strip()

inputs = [line.split(',') for line in inputs.split('\n') if line]


def get_data(a):
    yield from (tuple(int(s) for s in item.split('=')[1].split('..')) for item in a)
    yield a[0].split(' ')[0]


def overlap(c1, c2):
    result = []
    for coord in range(3):
        pair = tuple(sorted(c1[coord] + c2[coord])[1:3])
        m = mean(pair)
        if c1[coord][0] <= m <= c1[coord][1] and c2[coord][0] <= m <= c2[coord][1]:
            result.append(pair)
        else:
            return None
    return tuple(result)


result = Counter()

cuboids = [tuple(get_data(a)) for a in inputs]
for i, curr in enumerate(cuboids):
    upd = Counter()
    for prev in result:
        o = overlap(curr, prev)
        if o:
            upd[o] -= result[prev]
    if curr[3] == 'on':
        upd[curr] += 1
    result.update(upd)

v = 0
for key in result:
    v += prod(abs(key[i][1] - key[i][0]) + 1 for i in range(3)) * result[key]

print(v)
