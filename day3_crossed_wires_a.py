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

def build_hash(wire):
    path = set()
    curr = (0, 0)
    for p in wire:
        dir = p[0]
        dist = int(p[1:])
        curr = update_set(path, curr, dir, dist)
    return path

if __name__ == '__main__':
    file = open('day3_input.txt', 'r')
    wires = file.read().split()
    wire1 = wires[0].split(',')
    wire2 = wires[1].split(',')

    path1 = build_hash(wire1)
    path2 = build_hash(wire2)

    intersections = []
    for point in path1:
        if point in path2:
            intersections.append(point)
    intersections.remove((0,0))
    closest_point = min(intersections, key = lambda x: abs(x[0]) + abs(x[1]))

    print('Closest point to (0, 0) = {}, Manhattan Distance = {}'
            .format(closest_point, abs(closest_point[0]) + abs(closest_point[1])))
