import heapq
import sys
from math import prod
from pathlib import Path

inputs = Path(sys.argv[1]).read_text().split('\n')
adjacents_d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
matrix = [[int(ch) for ch in line] for line in inputs if line]
max_i = len(matrix)
max_j = len(matrix[0])
low_points = set()
for i in range(max_i):
    for j in range(max_j):
        adjacents = []
        for adj in adjacents_d:
            try:
                adjacents.append(matrix[i + adj[0]][j + adj[1]])
            except IndexError:
                pass
        if all(adj > matrix[i][j] for adj in adjacents):
            low_points.add((i, j))

basins = {}
for point in low_points:
    open_points = {point}
    closed_points = set()
    basins[point] = set()
    while open_points:
        next_open_points = set()
        closed_points |= open_points
        for open_point in open_points:
            basins[point].add(open_point)
            for d in adjacents_d:
                i = open_point[0] + d[0]
                j = open_point[1] + d[1]
                if i < 0 or j < 0 or i >= max_i or j >= max_j:
                    continue
                if (i, j) in closed_points:
                    continue
                if matrix[i][j] == 9:
                    continue
                next_open_points.add((i, j))
        open_points = next_open_points

largest_basins = heapq.nlargest(3, [len(value) for value in basins.values()])
print(prod(largest_basins))
