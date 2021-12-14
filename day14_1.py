import sys
from collections import Counter
from pathlib import Path

inputs = Path(sys.argv[1]).read_text()

polymer_template, pair_insertion = inputs.split('\n\n')
polymer_template = [p for p in polymer_template.split('\n') if p][0]
pair_insertion = dict([p.split(' -> ') for p in pair_insertion.split('\n') if p])

# print(polymer_template)
# print(pair_insertion)

for step in range(10):
    new_polymer_template = ''
    for i in range(len(polymer_template) - 1):
        current = polymer_template[i:i + 2]
        new_polymer_template += current[0] + pair_insertion[current] if current in pair_insertion else current[0]
    new_polymer_template += polymer_template[-1]
    polymer_template = new_polymer_template
    # print(f'Step {step + 1}')
    # print(polymer_template)

quantity = Counter(polymer_template)
min_quantity = min(quantity.values())
max_quantity = max(quantity.values())
print(f'Subtraction: {max_quantity} - {min_quantity} = {max_quantity - min_quantity}')
