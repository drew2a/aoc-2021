import ast
import sys
from collections import deque
from itertools import combinations, product
from pathlib import Path

from scipy.spatial.transform import Rotation

inputs = Path(sys.argv[1]).read_text().strip()

inputs = [s for s in inputs.split('\n\n') if s]
rotations = list(product([0, 90, 180, 270], repeat=3))

scanners = []
for scanner in inputs:
    points = [p for p in scanner.split('\n') if p]
    scanners.append(set(ast.literal_eval(p) for p in points[1:]))


def get_all_rotations(a):
    for r in rotations:
        pointer_gen = (Rotation.from_euler('xyz', r, degrees=True).apply(p).tolist() for p in a)
        yield frozenset(tuple(round(f) for f in p) for p in pointer_gen)


def manhattan_diff(t1, t2):
    return tuple(t1[i] - t2[i] for i in range(len(t1)))


def manhattan_distance(t1, t2):
    return sum(abs(i) for i in manhattan_diff(t1, t2))


def move(a, d):
    def add(t1, t2):
        return tuple(t1[i] + t2[i] for i in range(len(t1)))

    return {add(e, d) for e in a}


def get_relative(point, beacons_set, current_scanner):
    for rotated_scanner in set(get_all_rotations(current_scanner)):
        for p in rotated_scanner:
            md = manhattan_diff(point, p)
            relative_scanner = move(rotated_scanner, md)
            intersection = relative_scanner & beacons_set
            if len(intersection) >= 12:
                return md, relative_scanner
    return None


beacons = set(scanners[0])
max_scanner = 0
min_scanner = 0

scanners_in_manhattan = {(0, 0, 0)}
remaining_scanners = deque(scanners[1:])
while remaining_scanners:
    print(f'To process: {len(remaining_scanners)}')
    scanner = remaining_scanners.popleft()
    for p in beacons:
        relative = get_relative(p, beacons, scanner)
        if relative:
            scanners_in_manhattan.add(relative[0])
            beacons.update(relative[1])
            break
    else:
        remaining_scanners.append(scanner)

print(f'Beacons count: {len(beacons)}')
max_manhattan_distance = 0
for c in combinations(scanners_in_manhattan, 2):
    distance = manhattan_distance(*c)
    if distance > max_manhattan_distance:
        max_manhattan_distance = distance

print(f'Max manhattan distance: {max_manhattan_distance}')
