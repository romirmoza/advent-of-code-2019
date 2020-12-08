from intcode_computer import intcode_computer
import numpy as np
from matplotlib import pyplot as plt

def move_robot(robot, dir):
    if dir:
        robot[1] -= 90
    else:
        robot[1] += 90
    angle = robot[1] % 360
    x, y = robot[0]
    if angle == 0:
        x += 1
    elif angle == 90:
        y += 1
    elif angle == 180:
        x -= 1
    elif angle == 270:
        y -= 1
    robot[0] = (x, y)
    return robot

def run_emergency_hull_painting_robot(input, robot_state):
    whites = set()
    visited = set()
    computer = intcode_computer(intcode, input)
    while 1:
        computer.intcode_parse_until_output()
        computer.intcode_parse_until_output()
        if computer.has_halted():
            break
        color, dir = list(map(int, computer.get_output().split()))
        visited.add(robot_state[0])
        whites.add(robot_state[0]) if color else whites.discard(robot_state[0])
        robot_state = move_robot(robot_state, dir)
        input = [1] if robot_state[0] in whites else [0]
        computer.extend_input(input)
        computer.clear_output()
    return whites, visited

def plot_registration_identifier(whites):
    max_x = max(p[0] for p in whites)
    max_y = max(p[1] for p in whites)
    min_x = min(p[0] for p in whites)
    min_y = min(p[1] for p in whites)

    id = np.zeros((max_x - min_x + 1, max_y - min_y + 1))
    for p in whites:
        id[p[0] - min_x, max_y - p[1]] = 1

    plt.imshow(id.T, cmap='gray')
    plt.show()
    return

if __name__ == '__main__':
    file = open('day11_input.txt', 'r')
    intcode = list(map(int, file.read().split(',')))

    # part a
    input = [0]
    robot_state = [(0, 0), 90]      # robot intial coordinates, orientation
    whites, visited = run_emergency_hull_painting_robot(input, robot_state)

    print('Number of panels visited = {}'.format(len(visited)))

    # part b
    input = [1]
    robot_state = [(0, 0), 90]      # robot intial coordinates, orientation
    whites, visited = run_emergency_hull_painting_robot(input, robot_state)

    plot_registration_identifier(whites)

