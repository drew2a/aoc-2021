import sys
from pathlib import Path

fish_population = [int(value) for value in Path(sys.argv[1]).read_text().split(',')]
# print(f'Day 0: {fish_population}')

for day in range(80):
    for i in range(len(fish_population)):
        if fish_population[i] > 0:
            fish_population[i] = fish_population[i] - 1
        elif fish_population[i] == 0:
            fish_population[i] = 6
            fish_population.append(8)

    # print(f'Day {day + 1}: {fish_population} ({len(fish_population)})')
print(f'Total: {len(fish_population)}')