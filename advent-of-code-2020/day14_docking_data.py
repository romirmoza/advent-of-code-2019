import re

def get_address_list(address, floating):
    address_list = []
    if not floating:
        return [address]
    idx = floating[0]
    address_list.extend(get_address_list(address & ~(1 << idx), floating[1:]))
    address_list.extend(get_address_list(address | (1 << idx), floating[1:]))
    return address_list

def apply_mask_to_value(value, mask):
    mask = list(mask)
    mask.reverse()
    for idx, bit in enumerate(mask):
        if bit == '0':
            value = value & ~(1 << idx)
        elif bit == '1':
            value = value | (1 << idx)
    return value

def apply_mask_to_address(address, mask):
    sz = len(mask)
    address_list = []
    address = address | int(mask.replace('X', '1'), 2) # Mask with Xs removed
    floating = [sz - idx - 1 for idx, bit in enumerate(mask) if bit == 'X']
    return get_address_list(address, floating)

def run_initialization_program(program, type='value'):
    mem = {}
    x=[]
    for line in program:
        if re.search('^mem', line):
            index = int(re.search('\[([0-9]*)\]', line).group(1))
            value = int(re.search('= ([0-9]*)', line).group(1))
            if type == 'value':
                value = apply_mask_to_value(value, mask)
                mem[index] = value
            elif type == 'address':
                index_list = apply_mask_to_address(index, mask)
                for idx in index_list:
                    mem[idx] = value
        elif re.search('^mask', line):
            mask = re.search('= (.*)', line).group(1)
    return mem

if __name__ == '__main__':
    file = open('day14_input.txt', 'r')
    initialization_program = list(file.read().split('\n'))

    mem1 = run_initialization_program(initialization_program, 'value')
    mem2 = run_initialization_program(initialization_program, 'address')

    print('Sum of all values = {}'.format(sum(mem1.values())))
    print('Sum of all values = {}'.format(sum(mem2.values())))