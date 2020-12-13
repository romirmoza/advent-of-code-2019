import copy

def count_adjacent_occupied(grid, i, j):
    rows = len(grid)
    cols = len(grid[0])
    neighbors = [grid[i + x][j + y] for x in (-1,0,1) for y in (-1,0,1) if (x != 0 or y != 0) and i+x<rows
                                                                                              and i+x>=0
                                                                                              and j+y<cols
                                                                                              and j+y>=0]
    return neighbors.count('#')


def count_visible_occupied(grid, i, j):
    rows = len(grid)
    cols = len(grid[0])
    neighbors = []
    for x in (-1,0,1):
        for y in (-1,0,1):
            if x != 0 or y != 0:
                c = 1
                while i+c*x<rows and i+c*x>=0 and j+c*y<cols and j+c*y>=0:
                    if grid[i + c * x][j + c * y]=='.':
                        c += 1
                        continue
                    neighbors.append(grid[i + c*x][j + c*y])
                    break
    return neighbors.count('#')

def step(grid, rule):
    new_grid = []
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        row = ''
        for j in range(cols):
            if grid[i][j]=='L' and rule =='adjacent' and not count_adjacent_occupied(grid, i, j):
                row += '#'
            elif grid[i][j]=='L' and rule =='visible' and not count_visible_occupied(grid, i, j):
                row += '#'
            elif grid[i][j]=='#' and rule =='adjacent' and count_adjacent_occupied(grid, i, j) >= 4:
                row += 'L'
            elif grid[i][j]=='#' and rule =='visible' and count_visible_occupied(grid, i, j) >= 5:
                row += 'L'
            else:
                row += grid[i][j]
        new_grid.append(row)
    return new_grid

def run_simulation_till_steady(grid, rule='adjacent'):
    new_grid = step(grid, rule)
    steps = 1
    while new_grid != grid:
        grid = new_grid
        new_grid = step(grid, rule)
        steps += 1
    return new_grid, steps

if __name__ == '__main__':
    file = open('day11_input.txt', 'r')
    grid = list(file.read().split('\n'))

    final_grid, steps = run_simulation_till_steady(grid)
    occupied = sum([row.count('#') for row in final_grid])

    print('Occupied seats = {}, at the steady state reached in steps = {}'.format(occupied, steps))

    final_grid, steps = run_simulation_till_steady(grid, 'visible')
    occupied = sum([row.count('#') for row in final_grid])

    print('Occupied seats = {}, at the steady state reached in steps = {}'.format(occupied, steps))