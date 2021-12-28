import sys
from pathlib import Path

inputs = '''
v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>
'''
inputs = Path(sys.argv[1]).read_text().strip()

inputs = [list(line) for line in inputs.split('\n') if line]
area = inputs

max_i = len(area)
max_j = len(area[0])
step = 0
while True:
    step += 1
    cucumbers_didnt_move = True
    for sub_step in range(2):
        new_area = [['.' for _ in range(max_j)] for _ in range(max_i)]
        for i in range(max_i):
            for j in range(max_j):
                if area[i][j] == '.':
                    continue

                next_j = (j + 1) % max_j if sub_step == 0 else j
                next_i = (i + 1) % max_i if sub_step == 1 else i
                target = '>' if sub_step == 0 else 'v'
                if area[next_i][next_j] == '.' and area[i][j] == target:
                    new_area[next_i][next_j] = area[i][j]
                    cucumbers_didnt_move = False
                else:
                    new_area[i][j] = area[i][j]

        area = new_area
    if cucumbers_didnt_move:
        break
print(f'{step}')
