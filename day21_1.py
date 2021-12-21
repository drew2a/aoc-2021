from itertools import cycle

players_info = {'1': (6, 0),
                '2': (2, 0)}
players = cycle('12')
dice = cycle(range(1, 101))
for turn, p in enumerate(players):
    info = players_info[p]
    roll = sum([next(dice) for _ in range(3)])
    space = (info[0] + roll) % 10
    score = info[1] + space + 1
    players_info[p] = (space, score)
    if score >= 1000:
        break

print(f'Result: {players_info[next(players)][1] * (turn + 1) * 3}')
