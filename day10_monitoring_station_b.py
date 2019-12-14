import numpy as np
import math

def get_polar(vector):
    x = vector[0]
    y = vector[1]
    dist = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)
    if theta > np.pi / 2:
        theta -= 2 * np.pi
    return dist, theta

def get_unit_vector(vector):
    x = vector[0]
    y = vector[1]
    return (round(x / math.sqrt(x**2 + y**2), 6), round(y / math.sqrt(x**2 + y**2), 6))

def count_visible_asteroids(asteroid, asteroid_list):
    direction_vector_list = []
    for ast in asteroid_list:
        if ast != asteroid:
            direction_vector = ((ast[0] - asteroid[0]) , (ast[1] - asteroid[1]))
            direction_vector = get_unit_vector(direction_vector)
            direction_vector_list.append(direction_vector)
    direction_vector_set = set(direction_vector_list)
    return len(direction_vector_set)

def get_order_from_polar(theta_list, tol=10**-6):
    theta_list = sorted(theta_list, key=lambda x: (-x[1], x[0]))
    order_list = []
    skip_list = []
    new_rotation = True
    while theta_list or skip_list:
        if not theta_list:
            new_rotation = True
            theta_list = skip_list
            skip_list = []
        ast = theta_list.pop(0)
        if new_rotation:
            order_list.append(ast)
            new_rotation = False
        else:
            if abs(order_list[-1][1] - ast[1]) < tol:
                skip_list.append(ast)
            else:
                order_list.append(ast)
    order_list = [x[2] for x in order_list]
    return order_list

def vaporization_order(asteroid, asteroid_list):
    theta_list = []
    for ast in asteroid_list:
        if ast != asteroid:
            direction_vector = ((ast[0] - asteroid[0]) , -(ast[1] - asteroid[1]))
            dist, theta = get_polar(direction_vector)
            theta_list.append([dist, theta, ast])

    order_list = get_order_from_polar(theta_list)
    return order_list


if __name__ == '__main__':
    N = 200
    file = open('day10_input.txt', 'r')
    input_map = file.read().split()

    asteroid_list = []
    for i, row in enumerate(input_map):
        asteroid_list.extend([(j, i) for j, x in enumerate(list(row)) if x == '#'])

    max_count = 0
    for asteroid in asteroid_list:
        count = count_visible_asteroids(asteroid, asteroid_list)
        if count > max_count:
            max_count = count
            max_count_asteroid = asteroid

    print('Best location for a new monitoring station = {}, visible asteroids = {}'.format(max_count_asteroid, max_count))

    order_list = vaporization_order(max_count_asteroid, asteroid_list)

    print('Vaporization Order = ')
    for i, x in enumerate(order_list):
        print('Vaporizated asteriod number {0:>3} = {1}'.format(i+1, x))

    answer = order_list[N-1][0] * 100 + order_list[N-1][1]
    print('Answer = {}'.format(answer))
