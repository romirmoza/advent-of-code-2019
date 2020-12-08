import numpy as np

def count_trees(grid, stepx=3, stepy=1):
    count = 0
    idx, idy = 0,0
    lenx, leny = len(grid[0]), len(grid)
    while idy < leny:
        if grid[idy][idx] == '#':
            count+=1
        idx, idy = (idx+stepx)%lenx, idy+stepy
    return count
    
if __name__ == '__main__':
    file = open('day3_input.txt', 'r')
    grid = list(file.read().split('\n'))
    step_list = [(1, 1), (3, 1), (5, 1), (7,1), (1, 2)]

    tree_count = count_trees(grid)
    prod_count = np.prod([count_trees(grid, s[0], s[1]) for s in step_list])

    print('Number of trees found = {}'.format(tree_count))
    print('Number of trees found = {}'.format(prod_count))
