import sys
from pathlib import Path

a = [item for item in Path(sys.argv[1]).read_text().split('\n') if item]

max_bit_count = 12
bit_counter = [0] * max_bit_count
for value in a:
    for i in range(max_bit_count):
        bit_counter[i] += 1 if value[i] == '1' else -1

gamma = 0
epsilon = 0
for i in range(max_bit_count):
    bit = min(1, (max(0, bit_counter[i])))
    gamma |= bit << max_bit_count - i - 1
    epsilon |= (not bit) << max_bit_count - i - 1

print(f'Result: {gamma * epsilon}')
