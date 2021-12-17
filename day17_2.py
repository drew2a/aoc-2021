inputs = 'target area: x=20..30, y=-10..-5'
inputs = 'target area: x=206..250, y=-105..-57'
splitted = inputs.split(', y=')
y_range = tuple(int(s) for s in splitted[1].split('..'))
x_range = [int(s) for s in splitted[0].split('x=')[1].split('..')]


def shot(x_velocity, y_velocity):
    x, y = 0, 0
    while x <= x_range[1] and y >= y_range[0]:
        x += x_velocity
        y += y_velocity

        if x_range[1] >= x >= x_range[0] and y_range[1] >= y >= y_range[0]:
            return True

        y_velocity -= 1
        if x_velocity < 0:
            x_velocity += 1
        elif x_velocity > 0:
            x_velocity -= 1

    return False


lowest_possible_x_velocity = 0
x = x_range[0]
while x > 0:
    lowest_possible_x_velocity += 1
    x -= lowest_possible_x_velocity

x_set = set(range(lowest_possible_x_velocity, x_range[1] + 1))
y_set = set(range(y_range[0], abs(y_range[0])))
result_set = set()
for x in x_set:
    for y in y_set:
        if shot(x, y):
            result_set.add((x, y))
print(len(result_set))
