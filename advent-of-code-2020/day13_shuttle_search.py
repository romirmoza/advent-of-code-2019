import numpy as np

def wait_time(time_stamp, id):
    return id - (time_stamp % id)

def find_earliest_id(time_stamp, bus_ids):
    return bus_ids[np.argmin([wait_time(time_stamp, id[1]) for id in bus_ids])]

def find_earliest_time_stamp(bus_ids):
    time_stamp, increment = 0, 1
    for bus_id in bus_ids:
        offset, id = (bus_id[1] - bus_id[0]) % bus_id[1], bus_id[1]
        while time_stamp % id  != offset:
            time_stamp += increment
        increment *= id
    return time_stamp

if __name__ == '__main__':
    file = open('day13_input.txt', 'r')
    time_stamp, bus_ids = list(file.read().split('\n'))

    time_stamp = int(time_stamp)
    bus_ids = [(index, int(id)) for index, id in enumerate(bus_ids.split(',')) if id != 'x']

    _, earliest_id = find_earliest_id(time_stamp, bus_ids)
    earliest_time_stamp =  find_earliest_time_stamp(bus_ids)

    print('Earliest bus id x Wait time = {}'.format(earliest_id * wait_time(time_stamp, earliest_id)))
    print('Earliest time stamp = {}'.format(earliest_time_stamp))