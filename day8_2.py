import sys
from pathlib import Path


def get_codes(sequence):
    digits = {}
    digits_lengths = {}
    source = {}

    encoded_symbols = [set(item) for item in sequence.split(' ') if item]
    for symbol in encoded_symbols:
        digits_lengths[len(symbol)] = symbol
    digits[1] = digits_lengths[2]
    digits[4] = digits_lengths[4]
    digits[7] = digits_lengths[3]
    digits[8] = digits_lengths[7]

    source['a'] = digits[7] - digits[1]

    for digit in digits:
        encoded_symbols.remove(digits[digit])

    for symbol in encoded_symbols:
        s = symbol - digits[7] - digits[4]
        if len(s) == 1:
            source['g'] = s
            break

    digits[9] = digits[4] | source['a'] | source['g']
    source['e'] = digits[8] - digits[9]
    encoded_symbols.remove(digits[9])

    intersection = []
    six_digits = []
    for symbol in encoded_symbols:
        if len(symbol) == 5:
            intersection.append(symbol)
            if source['e'] < symbol:
                digits[2] = symbol
        else:
            six_digits.append(symbol)

    source['d'] = set.intersection(*intersection) - source['a'] - source['g']
    digits[0] = digits[8] - source['d']
    six_digits.remove(digits[0])
    digits[6] = six_digits[0]
    encoded_symbols.remove(digits[6])
    encoded_symbols.remove(digits[0])
    encoded_symbols.remove(digits[2])

    source['c'] = digits[1] - digits[6]
    for symbol in encoded_symbols:
        if source['c'] < symbol:
            digits[3] = symbol
            break
    encoded_symbols.remove(digits[3])
    digits[5] = encoded_symbols[0]

    return digits


def decode(s, codes):
    for item in s.split(' '):
        s = set(item)
        for digit in codes:
            if codes[digit] == s:
                yield digit


s = 0
for line in Path(sys.argv[1]).read_text().split('\n'):
    print(line)
    if not line:
        continue
    inputs, outputs = line.split('|')
    codes = get_codes(inputs)
    decoded = ''.join(list(str(i) for i in decode(outputs, codes)))
    s += int(decoded)

print(f'Count: {s}')
