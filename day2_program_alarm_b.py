import copy
from intcode_computer import intcode_computer

if __name__ == '__main__':
    desired_output = 19690720
    file = open('day2_input.txt', 'r')
    intcode_inital = map(int, file.read().split(','))

    found = 0
    for noun in range(100):
        for verb in range(100):
            intcode = copy.deepcopy(intcode_inital)
            computer = intcode_computer(intcode)
            computer.alarm1202(noun, verb)
            computer.intcode_parser()
            if computer.get_intcode()[0] == desired_output:
                found = 1
                break
        if found:
            break

    result = 100 * noun + verb
    print('Output of the IntCode = {}'.format(computer.get_intcode()[0]))
    print('Noun = {} and Verb = {}'.format(noun, verb))
    print('Result = {}'.format(result))
