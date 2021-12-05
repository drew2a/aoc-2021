import sys
from collections import defaultdict
from pathlib import Path
from types import SimpleNamespace

inputs = Path(sys.argv[1]).read_text().split('\n')


def create_point(raw_point):
    a = raw_point.split(',')
    return SimpleNamespace(x=int(a[0]), y=int(a[1]))


def get_distance_and_step(start, stop):
    distance = start - stop
    if not distance:
        return distance, 0

    return (distance - 1, 1) if distance < 0 else (distance + 1, -1)


inputs = [[create_point(point) for point in item.split(' -> ')] for item in inputs if item]
intersections = defaultdict(int)

for line in inputs:
    start = line[0]
    stop = line[1]

    is_diagonal = abs(start.x - stop.x) == abs(start.y - stop.y)
    if start.x == stop.x or start.y == stop.y or is_diagonal:
        x_distance, x_increment = get_distance_and_step(start.x, stop.x)
        y_distance, y_increment = get_distance_and_step(start.y, stop.y)

        while x_distance != 0 or y_distance != 0:
            if x_distance != 0:
                x_distance += x_increment
            if y_distance != 0:
                y_distance += y_increment
            intersections[(start.x - x_distance, start.y - y_distance)] += 1

print(f"Two and more: {len([key for key in intersections if intersections[key] >= 2])}")
