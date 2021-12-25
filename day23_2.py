import time
from copy import deepcopy

_rooms = [
    (list('CDDB'), 'A', 1),
    (list('CBCB'), 'B', 3),
    (list('AABD'), 'C', 5),
    (list('ACAD'), 'D', 7),
]

w = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000,
}
room_length = len(_rooms[0][0])

_hallway = [[None, None]] + list(([None]) for _ in range(7)) + [[None, None]]


def right_room(room, letter, amphipod):
    return letter == amphipod and all(a == amphipod for a in room)


def game_over(rooms):
    return all(len(r) == room_length for r, _, __ in rooms) and all(all(am == a for am in r) for r, a, _ in rooms)


def can_go(start_index, end_index, hallway):
    si = min(start_index, end_index)
    mi = max(start_index, end_index) + 1
    return all(not h[0] for h in hallway[si:mi])


def score(start_room, dest_room, amphipod, hallength):
    s_r1 = room_length - len(start_room) if start_room is not None else 0
    s_r2 = 1 + room_length - len(dest_room) if dest_room is not None else 0
    sc = (hallength + s_r1 + s_r2) * w[amphipod]
    return sc


cache = set()


def action(rooms, hallway):
    unistr = hash(f'{hash(str(rooms))}:{hash(str(hallway))}')
    if unistr in cache:
        return None

    if game_over(rooms):
        return 0

    rooms = deepcopy(rooms)
    hallway = deepcopy(hallway)

    for hall_i in range(len(hallway)):
        hall = hallway[hall_i]
        for inner_hall_i in range(len(hall)):
            if amphipod := hall[inner_hall_i]:
                hall[inner_hall_i] = None
                for dest_room, dest_a, dest_i in rooms:
                    if can_go(hall_i, dest_i, hallway) and right_room(dest_room, dest_a, amphipod):
                        dest_room.append(amphipod)
                        if (r := action(rooms, hallway)) is not None:
                            return score(None, dest_room, amphipod, inner_hall_i + abs(hall_i - dest_i)) + r
                        dest_room.pop()
                hall[inner_hall_i] = amphipod

    results = []
    for room, a, i in rooms:
        if not room or right_room(room, a, a):
            continue
        amphipod = room.pop()

        for dest_room, dest_a, dest_i in rooms:
            if dest_room != room and can_go(i, dest_i, hallway) and right_room(dest_room, dest_a, amphipod):
                dest_room.append(amphipod)
                if (r := action(rooms, hallway)) is not None:
                    return score(room, dest_room, amphipod, abs(dest_i - i)) + r
                dest_room.pop()

        for hall_i in [0, 2, 4, 6, 8]:
            hall = hallway[hall_i]
            if can_go(i, hall_i, hallway):
                for inner_hall_i in range(len(hall)):
                    if hall[inner_hall_i]:
                        break

                    hall[inner_hall_i] = amphipod
                    if (r := action(rooms, hallway)) is not None:
                        s = score(room, None, amphipod, inner_hall_i + abs(hall_i - i))
                        results.append(r + s)
                    hall[inner_hall_i] = None

        room.append(amphipod)

    if not results:
        cache.add(unistr)
        return None

    return min(results)


t = time.time()
results = action(_rooms, _hallway)
print(results)
print(f'Time: {time.time() - t}')
