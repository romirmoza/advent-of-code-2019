def has_same_adjacent(num):
    digits = [int(x) for x in str(num)]
    for i in range(len(digits)-1):
        if digits[i] == digits[i+1]:
            return True
    return False

def has_same_adjacent_pair_only(num):
    digits = [int(x) for x in str(num)]
    digits.insert(0, 'x')       # Pad digits
    digits.append('x')
    for i in range(1, len(digits)-1):
        if digits[i] == digits[i+1] and digits[i] != digits[i-1] and digits[i] != digits[i+2]:
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

    counta, countb = 0, 0
    for num in range(limi, limj + 1):
        if is_increasing(num) and has_same_adjacent(num):
            counta += 1
        if is_increasing(num) and has_same_adjacent_pair_only(num):
            countb += 1


    print('Count of valid passwords part a = {}'.format(counta))
    print('Count of valid passwords part b = {}'.format(countb))
