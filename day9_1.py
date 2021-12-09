import sys
from pathlib import Path

inputs = Path(sys.argv[1]).read_text().split('\n')

matrix = [[int(ch) for ch in line] for line in inputs if line]
low_points = []
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        adjacents = []
        for adj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            try:
                adjacents.append(matrix[i + adj[0]][j + adj[1]])
            except IndexError:
                pass
        if all(adj > matrix[i][j] for adj in adjacents):
            low_points.append(matrix[i][j])

print(low_points)
print(f'Sum of the risk: {sum(p + 1 for p in low_points)}')
