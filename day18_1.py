import ast
import re
import sys
from math import ceil, floor
from pathlib import Path

inputs = Path(sys.argv[1]).read_text().strip()
inputs = [s for s in inputs.split('\n') if s]


def find_pair_to_explode(s: str):
    nested = 0
    start = 0
    for i, ch in enumerate(s):
        if ch == '[':
            nested += 1
            start = i
        if ch == ']':
            nested -= 1
            if nested >= 4:
                return start, i
    return None


def add(s, n):
    def _add(m):
        value = m.group(0)
        return str(int(value) + int(n))

    return re.sub(r'\d+', _add, s, 1)


def add_left(s, n):
    end = 0
    for i in range(len(s) - 1, 0, -1):
        if s[i].isdigit() and not end:
            end = i
        if not s[i].isdigit() and end:
            return s[:i] + add(s[i:end + 1], n) + s[end + 1:]

    return s


def explode(s):
    indexes = find_pair_to_explode(s)
    if indexes:
        value = s[indexes[0] + 1:indexes[1]]
        pair = value.split(',')
        left = add_left(s[:indexes[0]], pair[0])
        right = add(s[indexes[1] + 1:], pair[1])
        return left + '0' + right
    return s


def split(s):
    def _split(m):
        value = m.group(0)
        i = int(value)
        if i > 9:
            first = floor(i / 2)
            second = ceil(i / 2)
            return f'[{first},{second}]'
        return value

    return re.sub(r'\d{2,}', _split, s, 1)


def reduce(s):
    while True:
        exploded = explode(s)
        if exploded != s:
            s = exploded
            continue
        splitted = split(s)
        if splitted != s:
            s = splitted
            continue
        break
    return s


def magnitude(s):
    def _magnitude(value, i):
        if isinstance(value, list):
            value = sum(_magnitude(item, i) for i, item in enumerate(value))
        if i is None:
            return value
        return value * 2 if i else value * 3

    a = ast.literal_eval(s)
    return _magnitude(a, None)


result = None
for sn in inputs:
    result = f'[{result},{sn}]' if result else sn
    result = reduce(result)
print(result)
print(magnitude(result))
