def has_same_adjacent(num):
    digits = [int(x) for x in str(num)]
    for i in range(len(digits)-1):
        if digits[i] == digits[i+1]:
            return True
    return False

def is_increasing(num):
    digits = [int(x) for x in str(num)]
    for i in range(len(digits)-1):
        if digits[i] > digits[i+1]:
            return False
    return True

if __name__ == '__main__':
    limi = 359282
    limj = 820401

    count = 0
    for num in range(limi, limj + 1):
        if is_increasing(num) and has_same_adjacent(num):
            count += 1

    print('Count of valid passwords = {}'.format(count))
