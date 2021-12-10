import sys
from pathlib import Path

inputs = Path(sys.argv[1]).read_text().split('\n')

chunk = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}
points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}
score = 0
for line in inputs:
    stack = []

    for ch in line:
        if ch in chunk:
            stack.append(ch)
            continue
        last_item = stack.pop()
        if chunk[last_item] != ch:
            score += points[ch]
            break

print(f'Score: {score}')
