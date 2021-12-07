import sys
from pathlib import Path

positions = [int(value) for value in Path(sys.argv[1]).read_text().split(',')]

min_position = min(positions)
max_position = max(positions)

min_fuel = min(sum(sum(range(abs(item - position) + 1)) for item in positions) for position in
               range(min_position, max_position + 1))
print(f'Min fuel: {min_fuel}')
