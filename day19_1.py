import ast
import sys
from collections import deque
from itertools import product
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
                return relative_scanner
    return None


beacons = set(scanners[0])
remaining_scanners = deque(scanners[1:])
while remaining_scanners:
    print(f'To process: {len(remaining_scanners)}')
    scanner = remaining_scanners.popleft()
    for p in beacons:
        relative_scanner = get_relative(p, beacons, scanner)
        if relative_scanner:
            beacons.update(relative_scanner)
            break
    else:
        remaining_scanners.append(scanner)

print(len(beacons))
