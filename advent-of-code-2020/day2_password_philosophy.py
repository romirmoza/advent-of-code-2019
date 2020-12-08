def decode_string(p):
    range, char, string = p.split()
    range_l, range_r = map(int, range.split('-'))
    l = char.rstrip(':')
    return range_l, range_r, l, string

def count_valid(passwords):
    valid = 0
    for p in passwords:
        min, max, l, string = decode_string(p)
        count = string.count(l)
        if count >= min and count <=max:
            valid += 1
    return valid

def index_valid(passwords):
    valid = 0
    for p in passwords:
        idx1, idx2, l, string = decode_string(p)
        if (string[idx1-1] == l) + (string[idx2-1] == l) == 1:
            valid += 1
    return valid

if __name__ == '__main__':
    file = open('day2_input.txt', 'r')
    passwords = list(file.read().split('\n'))

    count_valid = count_valid(passwords)
    index_valid = index_valid(passwords)

    print('Number of valid passwords = {}'.format(count_valid))
    print('Number of valid passwords = {}'.format(index_valid))
