import re
import sys
from itertools import chain
from pathlib import Path

inputs = [item for item in re.split(r'\n\n', Path(sys.argv[1]).read_text())]
dimension = 5


def matrix(s: str):
    horizontal_sets = [set() for _ in range(dimension)]
    vertical_sets = [set() for _ in range(dimension)]
    for i, line in enumerate(s.strip().split('\n')):
        for j, char in enumerate(re.split(r'\s+', line.strip())):
            integer = int(char)
            vertical_sets[j].add(integer)
            horizontal_sets[i].add(integer)
    return horizontal_sets, vertical_sets


def play(boards, random_sequence):
    for number in random_sequence:
        for board in boards:
            for board_set in board:
                for s in board_set:
                    s.discard(number)

                    if len(s) == 0:
                        return sum(chain.from_iterable(board_set)) * number
    return 0


random_sequence = [int(ch) for ch in inputs[0].split(',')]
boards = [matrix(board) for board in inputs[1:]]
# print(f'Sequence: {random_sequence}')
# print(f'Boards: {boards}')

print(play(boards, random_sequence))
