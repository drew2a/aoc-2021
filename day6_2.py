import sys
from collections import defaultdict
from pathlib import Path

fish_population = [int(value) for value in Path(sys.argv[1]).read_text().split(',')]
fish_groups = defaultdict(int)
for fish in fish_population:
    fish_groups[fish] += 1

for day in range(256):
    new_group = defaultdict(int)
    for fish in fish_groups:
        if fish > 0:
            new_group[fish - 1] += fish_groups[fish]
        elif fish == 0:
            new_group[6] += fish_groups[fish]
            new_group[8] += fish_groups[fish]
    fish_groups = new_group

print(f'Total: {sum(fish_groups.values())}')
