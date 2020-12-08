from math import log

def get_row_col(p, row_size, col_size):
    row_idx = p[0:int(log(row_size, 2))]
    col_idx = p[int(log(row_size, 2)):]
    row_left, row_right = 0, row_size-1
    for r in row_idx:
        if r == 'F':
                row_right -= (row_right - row_left + 1) / 2
        elif r == 'B':
                row_left += (row_right - row_left + 1) / 2
    col_left, col_right = 0, col_size-1
    for c in col_idx:
        if c == 'L':
                col_right -= (col_right - col_left + 1) / 2
        elif c == 'R':
                col_left += (col_right - col_left + 1) / 2
    return row_left, col_left

def find_max_seat_id(partitions, row_size, col_size):
    max_seat_id = 0
    for p in partitions:
        row, col = get_row_col(p, row_size, col_size)
        seat_id = row * col_size + col
        max_seat_id = max_seat_id if max_seat_id > seat_id else seat_id
    return max_seat_id

def get_seat_id_list(partitions, row_size, col_size):
    seat_id_list = []
    for p in partitions:
        row, col = get_row_col(p, row_size, col_size)
        seat_id = row * col_size + col
        seat_id_list.append(seat_id)
    return seat_id_list

if __name__ == '__main__':
    file = open('day5_input.txt', 'r')
    partitions = list(file.read().split('\n'))
    max_seat_id = find_max_seat_id(partitions, 128, 8)
    seat_id_list = get_seat_id_list(partitions, 128, 8)
    seat_id_list = sorted(seat_id_list)

    for id in seat_id_list:
        if id + 1 not in seat_id_list and id + 2 in seat_id_list:
            my_seat_id = id + 1

    print('Highest seat ID = {}'.format(max_seat_id))
    print('My seat ID = {}'.format(my_seat_id))
    

