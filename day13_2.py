import sys
from pathlib import Path

inputs = Path(sys.argv[1]).read_text()

coordinates, folds = inputs.split('\n\n')
coordinates_set = set(tuple(int(ch) for ch in c.split(',')) for c in coordinates.split('\n') if c)
folds_list = list(f[11:] for f in folds.split('\n') if f)


def print_dots():
    max_x = max(c[0] for c in coordinates_set)
    max_y = max(c[1] for c in coordinates_set)
    for y in range(max_y + 1):
        line = ['#' if (x, y) in coordinates_set else '.' for x in range(max_x + 1)]
        print(''.join(line))


for fold in folds_list:
    axis, digit = fold.split('=')
    digit = int(digit)
    new_coordinates_set = set()
    for c in coordinates_set:
        def fold_it(d, c):
            return d - abs(d - c)

        coord = (c[0], fold_it(digit, c[1])) if axis == 'y' else (fold_it(digit, c[0]), c[1])
        new_coordinates_set.add(coord)

    coordinates_set = new_coordinates_set

print_dots()
