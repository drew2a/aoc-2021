import sys
from pathlib import Path

a = [item.split(' ') for item in Path(sys.argv[1]).read_text().split('\n') if item]
position = 0
depth = 0
aim = 0
for i in range(0, len(a)):
    key = a[i][0]
    value = int(a[i][1])
    if key == 'forward':
        position += value
        depth += aim * value
    if key == 'down':
        aim += value
    if key == 'up':
        aim -= value

print(position * depth)
