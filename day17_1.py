inputs = 'target area: x=206..250, y=-105..-57'
splitted = inputs.split(', y=')
x_range = [int(s) for s in splitted[0].split('x=')[1].split('..')]
y_range = [int(s) for s in splitted[1].split('..')]

for finish_y_velocity in range(y_range[0] - 1, y_range[1]):
    for possible_finish_y in range(y_range[0], y_range[1] + 1):
        y = possible_finish_y
        y_velocity = finish_y_velocity
        highest_y = 0
        while y > 0 or y_velocity < 0:
            y_velocity += 1
            y -= y_velocity
            if y > highest_y:
                highest_y = y
        if y == 0:
            print(f'Bingo: y={y_velocity} stopped at {possible_finish_y} with v={finish_y_velocity}')
            print(f'Highest y: {highest_y}')
            break
    else:
        continue
    break
