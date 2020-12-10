from itertools import combinations
from collections import defaultdict

def check_xmas_property(data, preamble_len):
    for i in range(len(data)):
        if i < preamble_len: continue
        possible_sums = list(map(lambda x: x[0]+x[1], combinations(data[i-preamble_len:i], 2)))
        if data[i] not in possible_sums:
            return data[i]
    return

def contiguous_sum(data, target):
    for i in range(len(data)):
        for j in range(i, len(data)):
            if sum(data[i:j+1]) == target:
                return data[i:j+1]
            if sum(data[i:j+1]) > target:
                break
    return

def contiguous_sum_efficient(data, target):
    sum_dict = defaultdict(int)
    for i in range(len(data)): sum_dict[i] = sum_dict[i-1] + data[i]
    for i in range(len(data)):
        if sum_dict[i] == target:
            return data[0:i+1]
        for key, val in sum_dict.items():
            if val == sum_dict[i] + target:
                return data[i:key+1]
    return

if __name__ == '__main__':
    file = open('day9_input.txt', 'r')
    data = list(map(int,file.read().split('\n')))
    preamble_len = 25

    first_num = check_xmas_property(data, preamble_len)
    seq = contiguous_sum_efficient(data, first_num)

    print('First number that doesnt follow the XMAS property = {}'.format(first_num))
    print('Encryption weakness = {}'.format(max(seq) + min(seq)))