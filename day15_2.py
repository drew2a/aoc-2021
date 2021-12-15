import sys
from pathlib import Path

inputs = Path(sys.argv[1]).read_text()

matrix = [[int(ch) for ch in line] for line in inputs.split('\n') if line]
max_x = len(matrix[0])
max_y = len(matrix)

big_matrix = []
for x in range(max_x * 5):
    small_x_index = x % max_x
    addition_x = int(x / max_x)
    line = []

    for y in range(max_y * 5):
        small_y_index = y % max_y
        addition_y = int(y / max_y)

        value = matrix[small_x_index][small_y_index] + addition_x + addition_y
        line.append(value if value <= 9 else value - 9)
    big_matrix.append(line)
matrix = big_matrix

max_x = len(matrix[0])
max_y = len(matrix)

scores = [[None for _ in range(max_x)] for _ in range(max_y)]
opened = {(0, 0)}
while opened:
    p = opened.pop()
    s = scores[p[0]][p[1]] or 0
    for adjacent in {(-1, 0), (1, 0), (0, -1), (0, 1)}:
        x = p[0] + adjacent[0]
        y = p[1] + adjacent[1]

        if x < 0 or y < 0 or y >= max_y or x >= max_x:
            continue

        score = s + matrix[x][y]
        new_point = (x, y)
        if (scores[x][y] is None) or scores[x][y] > score:
            opened.add(new_point)
            scores[x][y] = score

print(scores[max_x - 1][max_y - 1])
