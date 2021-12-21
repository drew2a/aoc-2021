from collections import defaultdict
from itertools import cycle, product

multiverse = defaultdict(int)
multiverse[((6, 0), (2, 0))] = 1
scores = defaultdict(int)
players = cycle([0, 1])
while multiverse:
    p = next(players)
    new_multiverse = defaultdict(int)
    for universe in multiverse:
        for roll in product([1, 2, 3], repeat=3):
            space, score = universe[p]
            space = (space + sum(roll)) % 10
            score += space + 1
            if score < 21:
                new_key = ((space, score), universe[1]) if p == 0 else (universe[0], (space, score))
                new_multiverse[new_key] += multiverse[universe]
            else:
                scores[p] += multiverse[universe]
    multiverse = new_multiverse
print(scores)
