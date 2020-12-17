from intcode_computer import intcode_computer

move_back = {1:2,
             2:1,
             3:4,
             4:3}
# moves to bring the robot back to where it started

def bfs(grid, source):
    dist = {source: 0}
    visited = {source}
    q = [source]
    while q:
        current = q.pop(0)
        moves_dict = {1: (current[0]  , current[1]+1),
                      2: (current[0]  , current[1]-1),
                      3: (current[0]-1, current[1]),
                      4: (current[0]+1, current[1])}
        for move, pos in moves_dict.items():
            if pos not in visited and grid.get(pos) not in ['U', '#']:
                q.append(pos)
                visited.add(pos)
                dist[pos] = dist[current] + 1
    return dist

def explore_map(computer, current, visited):
    x, y = source[0], source[1]
    # north (1), south (2), west (3), and east (4)
    moves_dict = {1: (current[0]  , current[1]+1),
                  2: (current[0]  , current[1]-1),
                  3: (current[0]-1, current[1]),
                  4: (current[0]+1, current[1])}
    for move, pos in moves_dict.items():
        if pos not in visited:
            computer.clear_output()
            computer.set_input([move])
            computer.intcode_parse_until_output()
            output = int(computer.get_output()[0])
            # print(visited, pos, output)
            if output == 0:
                visited[pos] = '#'
            elif output == 1:
                visited[pos] = '.'
                explore_map(computer, pos, visited)
                computer.set_input([move_back[move]])
                computer.intcode_parse_until_output()
            elif output == 2:
                visited[pos] = 'S'
                explore_map(computer, pos, visited)
                computer.set_input([move_back[move]])
                computer.intcode_parse_until_output()
    return

def print_grid(grid, buffer):
    min_x = min([x for x, y in grid])
    max_x = max([x for x, y in grid])
    max_y = max([y for x, y in grid])
    min_y = min([y for x, y in grid])
    for y in range(min_y - buffer, max_y + buffer + 1):
        row = []
        for x in range(min_x - buffer, max_x + buffer + 1):
            row.append(grid.get((x, y), 'U'))
        print(''.join(row))
    return

if __name__ == '__main__':
    file = open('day15_input.txt', 'r')
    intcode = list(map(int, file.read().split(',')))

    source = (0, 0)
    grid = {source: 'S'}
    computer = intcode_computer(intcode, [])
    explore_map(computer, (0, 0), grid)

    buffer = 0
    print_grid(grid, buffer)

    for key, val in grid.items():
        if val == 'S':
            oxygen_system_position = key
    dist = bfs(grid, oxygen_system_position)

    print('Position of the oxygen system = {}'.format(oxygen_system_position))
    print('Total time for oxygen to fill up the map = {}'.format(max(dist.values())))
