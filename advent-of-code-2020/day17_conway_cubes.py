def count_active_neighbors(node, active_cubes):
    # # 3D
    # x, y, z = node[0], node[1], node[2]
    # neighbor_list = [(x+a,y+b,z+c) for a in (-1,0,1) for b in (-1,0,1) for c in (-1,0,1) if (a != 0 or b != 0 or c!=0)]
    neighbor_list = get_neighbor_list(node, active_cubes, ())
    return sum([1 for neighbor in neighbor_list if neighbor in active_cubes])

def get_neighbor_list(node, active_cubes, neighbor):
    dim = len(neighbor) - len(node)
    neighbor_list = []

    if not dim:
        if neighbor != node:
            neighbor_list.append(neighbor)
        return neighbor_list

    for d in range(-1, 2):
        neighbor_list.extend(get_neighbor_list(node, active_cubes, neighbor + (node[dim]+d,)))
    return neighbor_list

def print_grid(active_cubes):
    min_x, max_x = min([c[0] for c in active_cubes]), max([c[0] for c in active_cubes])
    min_y, max_y = min([c[1] for c in active_cubes]), max([c[1] for c in active_cubes])
    min_z, max_z = min([c[2] for c in active_cubes]), max([c[2] for c in active_cubes])
    for z in range(min_z, max_z+1):
        print('z = {}'.format(z))
        for y in range(min_y, max_y+1):
            row = ''
            for x in range(min_x, max_x+1):
                if (x,y,z) in active_cubes:
                    row += '#'
                else:
                    row += '.'
            print(row)
    return

def next_state(active_cubes, dim, node):
    if not dim:
        next_active_cubes = set()
        if node in active_cubes and count_active_neighbors(node, active_cubes) in [2, 3]:
            next_active_cubes.add(node)
        if node not in active_cubes and count_active_neighbors(node, active_cubes) in [3]:
            next_active_cubes.add(node)
        return next_active_cubes

    next_active_cubes = set()
    min_d, max_d = min([c[-dim] for c in active_cubes]), max([c[-dim] for c in active_cubes])
    for d in range(min_d-1, max_d+2):
        next_active_cubes.update(next_state(active_cubes, dim-1, node + (d,)))
    return next_active_cubes

def run_cycles(active_cubes, num, dim):
    for i in range(num):
        active_cubes = next_state(active_cubes, dim, ())
    return active_cubes

def set_initial_state(input, dim):
    active_cubes = set()
    for y, row in enumerate(input):
        row = list(row)
        for x, val in enumerate(row):
            if val == '#':
                cube = (x,y)
                for i in range(dim-2):
                    cube += (0,)
                active_cubes.add(cube)
    return active_cubes

if __name__ == '__main__':
    file = open('day17_input.txt', 'r')
    input = list(file.read().split('\n'))
    cycles = 6

    dim = 3
    active_cubes = set_initial_state(input, dim)
    active_cubes = run_cycles(active_cubes, cycles, dim)
    print_grid(active_cubes)

    print('Active cubes after 6 cycles = {}'.format(len(active_cubes)))

    dim = 4
    active_cubes = set_initial_state(input, dim)
    active_cubes = run_cycles(active_cubes, cycles, dim)

    print('Active cubes after 6 cycles = {}'.format(len(active_cubes)))
