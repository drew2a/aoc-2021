import sys
from pathlib import Path

coordinates, folds = Path(sys.argv[1]).read_text().split('\n\n')
coordinates_set = set(tuple(int(ch) for ch in c.split(',')) for c in coordinates.split('\n') if c)
folds_list = list(f[11:] for f in folds.split('\n') if f)

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
    break

print(len(coordinates_set))
