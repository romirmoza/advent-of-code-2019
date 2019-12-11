def alarm1202(intcode, noun = 12, verb = 2):
    intcode[1] = noun
    intcode[2] = verb
    return 0

def intcode_parser(intcode):
    pc = 0
    while intcode[pc] != 99:
        if intcode[pc] == 1:
            intcode[intcode[pc + 3]] = intcode[intcode[pc + 1]] + intcode[intcode[pc + 2]]
            pc += 4
        elif intcode[pc] == 2:
            intcode[intcode[pc + 3]] = intcode[intcode[pc + 1]] * intcode[intcode[pc + 2]]
            pc += 4
    return 0

if __name__ == '__main__':
    file = open('day2_input.txt', 'r')
    intcode = map(int, file.read().split(','))

    alarm1202(intcode)
    intcode_parser(intcode)
    print('Output of the IntCode = {}'.format(intcode[0]))
