import sys
from collections import Counter, defaultdict
from pathlib import Path

inputs = Path(sys.argv[1]).read_text()

polymer_template, pair_insertion = inputs.split('\n\n')
polymer_template = list([p for p in polymer_template.split('\n') if p][0])


def get_polymer_pairs():
    result = defaultdict(int)
    for i in range(len(polymer_template) - 1):
        key = polymer_template[i] + polymer_template[i + 1]
        result[key] += 0.5
    return result


polymer_pairs = get_polymer_pairs()
pair_insertion = dict([p.split(' -> ') for p in pair_insertion.split('\n') if p])

for step in range(40):
    new_polymer_pairs = defaultdict(int)
    for pair in polymer_pairs:
        count = polymer_pairs[pair]
        insertion = pair_insertion.get(pair)
        if insertion:
            for new_pair in [pair[0] + insertion, insertion + pair[1]]:
                new_polymer_pairs[new_pair] += count
        else:
            new_polymer_pairs[pair] = count
    polymer_pairs = new_polymer_pairs

quantity = Counter()
for pair in polymer_pairs:
    count = polymer_pairs[pair]
    for ch in pair:
        quantity.update({ch: count})

min_quantity = min(quantity.values())
max_quantity = max(quantity.values())
result = max_quantity - min_quantity

print(f'Subtraction: {int(result) + 1}')
