import sys
from pathlib import Path
from statistics import median

# positions = [int(p) for p in '16,1,2,0,4,2,7,1,2,14'.split(',')]
positions = [int(value) for value in Path(sys.argv[1]).read_text().split(',')]

m = int(median(positions))
fuel = (abs(item - m) for item in positions)

print(f'Fuel: {sum(fuel)}')
#336701
