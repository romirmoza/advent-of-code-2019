import numpy as np
import math

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

if __name__ == '__main__':
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
