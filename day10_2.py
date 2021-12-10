import sys
from pathlib import Path
from statistics import median

inputs = [line for line in Path(sys.argv[1]).read_text().split('\n') if line]

chunk = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}
points = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}
scores = []
for line in inputs:
    stack = []

    for ch in line:
        if ch in chunk:
            stack.append(ch)
            continue
        last_item = stack.pop()
        if chunk[last_item] != ch:
            break
    else:
        score = 0
        for ch in reversed(stack):
            score *= 5
            score += points[ch]
        scores.append(score)
print(f'Median: {median(scores)}')
