def update_set(path, curr, dir, dist):
    if dir == 'U':
        path.update([(curr[0], curr[1] + y) for y in range(dist + 1)])
        curr = (curr[0], curr[1] + dist)
    if dir == 'D':
        path.update([(curr[0], curr[1] - y) for y in range(dist + 1)])
        curr = (curr[0], curr[1] - dist)
    if dir == 'L':
        path.update([(curr[0] - x, curr[1]) for x in range(dist + 1)])
        curr = (curr[0] - dist, curr[1])
    if dir == 'R':
        path.update([(curr[0] + x, curr[1]) for x in range(dist + 1)])
        curr = (curr[0] + dist, curr[1])
    return curr

def point_in_path(wire):
    path = set()
    curr = (0, 0)
    for p in wire:
        dir = p[0]
        dist = int(p[1:])
        curr = update_set(path, curr, dir, dist)
    return path

def path_length(wire, dest):
    curr = (0, 0)
    total_steps = 0
    for p in wire:
        dir = p[0]
        dist = int(p[1:])
        curr, steps = traverse_path(curr, dest, dir, dist)
        total_steps += steps
        if curr == dest:
            break
    return total_steps

def traverse_path(curr, dest, dir, dist):
    steps = dist
    if dir == 'U':
        if dest[0] == curr[0] and dest[1] - curr[1] <= dist:
            steps = dest[1] - curr[1]
            curr = (curr[0], dest[1])
        else:
            curr = (curr[0], curr[1] + dist)
    if dir == 'D':
        if dest[0] == curr[0] and curr[1] - dest[1] <= dist:
            steps = curr[1] - dest[1]
            curr = (curr[0], dest[1])
        else:
            curr = (curr[0], curr[1] - dist)
    if dir == 'L':
        if dest[1] == curr[1] and curr[0] - dest[0] <= dist:
            steps = curr[0] - dest[0]
            curr = (dest[0], curr[1])
        else:
            curr = (curr[0] - dist, curr[1])
    if dir == 'R':
        if dest[1] == curr[1] and dest[0] - curr[0] <= dist:
            steps = dest[0] - curr[0]
            curr = (dest[0], curr[1])
        else:
            curr = (curr[0] + dist, curr[1])
    return (curr, steps)

if __name__ == '__main__':
    file = open('day3_input.txt', 'r')
    wires = file.read().split()
    wire1 = wires[0].split(',')
    wire2 = wires[1].split(',')

    path1 = point_in_path(wire1) #set of points in path
    path2 = point_in_path(wire2)

    intersections = []
    for point in path1:
        if point in path2:
            intersections.append(point)
    intersections.remove((0,0))

    closest_point_by_distance = min(intersections, key = lambda x: abs(x[0]) + abs(x[1]))
    manhattan_distance = abs(closest_point_by_distance[0]) + abs(closest_point_by_distance[1])

    closest_point_by_steps = min(intersections, key = lambda x: path_length(wire1, x) + path_length(wire2, x))
    steps = path_length(wire1, closest_point_by_steps) + path_length(wire2, closest_point_by_steps)

    print('Closest point to (0, 0) by distance = {}, Manhattan Distance = {}'.format(closest_point_by_distance, manhattan_distance))
    print('Closest point to (0, 0) by steps = {}, ste = {}'.format(closest_point_by_steps, steps))
