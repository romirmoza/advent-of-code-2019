from collections import defaultdict

def run_code(code):
    pc = 0
    acc = 0
    visited = defaultdict(int)
    while pc < len(code):
        if visited[pc]:
            return 0, acc
        visited[pc] = 1
        line = code[pc]
        op, arg = line.split(' ')
        arg = int(arg)
        if op == 'acc':
            acc += arg
        elif op == 'jmp':
            pc += arg
            continue
        pc += 1
    return 1, acc

def fix_boot_code(boot_code):
    for i in range(len(boot_code)):
        if boot_code[i].split()[0] == 'jmp':
            boot_code[i] = boot_code[i].replace('jmp', 'nop')
            terminated, acc = run_code(boot_code)
            boot_code[i] = boot_code[i].replace('nop', 'jmp')
            if terminated:
                break

        if boot_code[i].split()[0] == 'nop':
            boot_code[i] = boot_code[i].replace('nop', 'jmp')
            terminated, acc = run_code(boot_code)
            boot_code[i] = boot_code[i].replace('jmp', 'nop')
            if terminated:
                return terminated, acc
    return terminated, acc

if __name__ == '__main__':
    file = open('day8_input.txt', 'r')
    boot_code = list(file.read().split('\n'))

    terminated, acc = run_code(boot_code) # part a
    terminated, acc = fix_boot_code(boot_code) # part b

    print('Accumulator before any instruction is executed a second time = {}'.format(acc))
    print('Accumulator when program terminated = {}'.format(acc))



