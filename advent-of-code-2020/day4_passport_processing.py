import re
from collections import defaultdict

def count_trees(grid, stepx=3, stepy=1):
    count = 0
    idx, idy = 0,0
    lenx, leny = len(grid[0]), len(grid)
    while idy < leny:
        if grid[idy][idx] == '#':
            count+=1
        idx, idy = (idx+stepx)%lenx, idy+stepy
    return count

def has_valid_fields(d):
    ecl_list = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    byr = int(d['byr'])
    iyr = int(d['iyr'])
    eyr = int(d['eyr'])
    if byr < 1920 or byr > 2002: return False
    if iyr < 2010 or iyr > 2020: return False
    if eyr < 2020 or eyr > 2030: return False
    if d['ecl'] not in ecl_list: return False

    if not re.search('^#[0-9a-f]{6}$', d['hcl']): return False
    if not re.search('^[0-9]{9}$', d['pid']): return False

    if re.search('^([0-9]*)cm$', d['hgt']):
        hgt = int(re.search('^([0-9]*)cm$', d['hgt']).group(1))
        if hgt < 150 or hgt > 193: return False
    elif re.search('^([0-9]*)in$', d['hgt']):
        hgt = int(re.search('^([0-9]*)in$', d['hgt']).group(1))
        if hgt < 59 or hgt > 76: return False
    else:
        return False
    return True

def is_valid_passport(p, keys_list, validate=False):
    d = defaultdict(int)
    fields = re.split(' |\n', p)
    for f in fields:
        key, val = f.split(':')
        d[key] = val
    for key in keys_list:
        if not d[key]:
            return 0
    if validate and not has_valid_fields(d):
        return 0
    return 1

if __name__ == '__main__':
    file = open('day4_input.txt', 'r')
    passports = list(file.read().split('\n\n'))
    keys_list = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'] #cid is ignored

    valid1, valid2 = 0, 0
    for p in passports:
        valid1 += is_valid_passport(p, keys_list)
        valid2 += is_valid_passport(p, keys_list, True)

    print('Number of valid passports = {}'.format(valid1))
    print('Number of valid passports = {}'.format(valid2))
