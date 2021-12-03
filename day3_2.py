import sys
from pathlib import Path

a = [item for item in Path(sys.argv[1]).read_text().split('\n') if item]

max_bit_count = 12
oxygen_generator_rating_set = set(range(len(a)))
CO2_scrubber_rating = set(range(len(a)))


def calculate_rating(condition):
    s = set(range(len(a)))
    for j in range(max_bit_count):
        set_0 = {index for index in s if a[index][j] == '0'}
        set_1 = {index for index in s if a[index][j] == '1'}
        bit_counter = len(set_1) - len(set_0)

        s &= set_0 if condition(bit_counter) else set_1
        if len(s) == 1:
            return a[s.pop()]


oxygen_generator_rating = calculate_rating(lambda b: b < 0)
CO2_scrubber_rating = calculate_rating(lambda b: b >= 0)

print(f'Oxygen generator rating: {oxygen_generator_rating}')
print(f'CO2 scrubber rating: {CO2_scrubber_rating}')

print(f'Result = {int(oxygen_generator_rating, 2) * int(CO2_scrubber_rating, 2)}')
