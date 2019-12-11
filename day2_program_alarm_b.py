import copy

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
    desired_output = 19690720
    file = open('day2_input.txt', 'r')
    intcode_inital = map(int, file.read().split(','))

    found = 0
    for noun in range(100):
        for verb in range(100):
            intcode = copy.deepcopy(intcode_inital)
            alarm1202(intcode, noun, verb)
            intcode_parser(intcode)
            if intcode[0] == desired_output:
                found = 1
                break
        if found:
            break

    result = 100 * noun + verb
    print('Output of the IntCode = {}'.format(intcode[0]))
    print('Noun = {} and Verb = {}'.format(noun, verb))
    print('Result = {}'.format(result))
