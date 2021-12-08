import sys
from pathlib import Path

positions = [int(value) for value in Path(sys.argv[1]).read_text().split(',')]

fuel_list = []
cache = {}


def calculate_fuel_for_position(position):
    for item in positions:
        normal_distance = abs(item - position) + 1
        if normal_distance in cache:
            distance = cache[normal_distance]
        else:
            distance = sum(range(normal_distance))
            cache[normal_distance] = distance
        yield distance


def assemble_fuel_list():
    for position in range(min(positions), max(positions) + 1):
        yield sum(calculate_fuel_for_position(position))


print(f'Min fuel: {min(assemble_fuel_list())}')
