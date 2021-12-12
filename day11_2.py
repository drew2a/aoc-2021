import sys
from pathlib import Path

inputs = [line for line in Path(sys.argv[1]).read_text().split('\n') if line]
matrix = [[int(ch) for ch in line] for line in inputs if line]
max_i = len(matrix)
max_j = len(matrix[0])
for step in range(1000):
    flashed = []
    flashed_count = 0

    for i in range(max_i):
        for j in range(max_j):
            matrix[i][j] += 1

            if matrix[i][j] < 10 or (i, j) in flashed:
                continue

            open_points = {(i, j)}
            while open_points:
                next_open_points = set()
                flashed.append((i, j))
                for open_point in open_points:
                    for di in range(-1, 2):
                        for dj in range(-1, 2):
                            ai = open_point[0] + di
                            aj = open_point[1] + dj
                            point = (ai, aj)
                            if ai < 0 or aj < 0 or ai >= max_i or aj >= max_j or point in flashed:
                                continue
                            matrix[ai][aj] += 1
                            if matrix[ai][aj] >= 10:
                                next_open_points.add(point)
                                flashed.append(point)

                open_points = next_open_points
    flashed_count = 0
    for i in range(max_i):
        for j in range(max_j):
            if matrix[i][j] >= 10:
                matrix[i][j] = 0
                flashed_count += 1
    if flashed_count == max_i * max_j:
        break
    # print(f'\nStep: {step + 1}')
    # print('\n'.join(','.join(str(ch) for ch in line) for line in matrix))

print(step + 1)
