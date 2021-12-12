import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import List, Set


@dataclass
class CavePath:
    path: List
    small_caves: Set
    ended: bool = False


inputs = [line.split('-') for line in Path(sys.argv[1]).read_text().split('\n') if line]
transitions = defaultdict(list)
for line in inputs:
    transitions[line[0]].append(line[1])
    transitions[line[1]].append(line[0])

paths = [CavePath(path=['start'], small_caves={'start'})]
while not all(p.ended for p in paths):
    new_paths = []

    for p in paths:
        last_point = p.path[-1]
        next_points = transitions[last_point]

        if last_point == 'end' or not next_points:
            new_paths.append(CavePath(path=p.path, ended=True, small_caves=p.small_caves))
            continue

        for next_point in next_points:
            small_caves = p.small_caves
            if next_point.islower():
                if next_point in p.small_caves:
                    continue
                small_caves = small_caves | {next_point}
            new_paths.append(CavePath(path=p.path + [next_point], small_caves=small_caves))
    paths = new_paths

print(f'Len: {len(paths)}')
