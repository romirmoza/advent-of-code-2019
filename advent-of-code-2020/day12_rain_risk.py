def manhattan_distance(state1, state2):
    x1, y1 = state1[0]
    x2, y2 = state2[0]
    return abs(x2-x1) + abs(y2-y1)

def move(state, action, value):
    (x, y), theta = state[0], state[1]
    if action == 'N': y += value
    if action == 'S': y -= value
    if action == 'E': x += value
    if action == 'W': x -= value
    if action == 'R': theta += value
    if action == 'L': theta -= value
    if action == 'F':
        angle = theta % 360
        if angle == 0: y += value
        elif angle == 90: x += value
        elif angle == 180: y -= value
        elif angle == 270: x -= value
    state = [(x, y), theta]
    return state

def move_with_waypoint(state, action, value):
    (x, y), (x_way, y_way) = state[0], state[1]
    if action == 'N': y_way += value
    if action == 'S': y_way -= value
    if action == 'E': x_way += value
    if action == 'W': x_way -= value
    if action == 'R':
        angle = value % 360
    if action == 'L':
        angle = -value % 360
    if action == 'R' or action == 'L':
        if angle == 90: x_way, y_way = y_way, -x_way
        elif angle == 180: x_way, y_way = -x_way, -y_way
        elif angle == 270: x_way, y_way = -y_way, x_way
    if action == 'F':
        x += x_way * value
        y += y_way * value
    state = [(x, y), (x_way, y_way)]
    return state

def execute_instructions(instructions, state, with_waypoint=False):
    for action, value in instructions:
        if with_waypoint:
            state = move_with_waypoint(state, action, value)
        else:
            state = move(state, action, value)
    return state

if __name__ == '__main__':
    file = open('day12_input.txt', 'r')
    instructions = list(map(lambda x: (x[0], int(x[1:])), file.read().split('\n')))

    initial_state = [(0, 0), 90]      # ship's intial coordinates, orientation
    final_state = execute_instructions(instructions, initial_state)

    print('Manhattan distance between initial and final locations = {}'.format(manhattan_distance(initial_state, final_state)))

    initial_state = [(0, 0), (10, 1)]      # ship's intial coordinates, relative location of waypoint
    final_state = execute_instructions(instructions, initial_state, 1)

    print('Manhattan distance between initial and final locations = {}'.format(manhattan_distance(initial_state, final_state)))