from intcode_computer import intcode_computer
import copy

def set_alarm_and_parse(intcode):
    computer = intcode_computer(intcode)
    computer.set_alarm(54,85)
    computer.intcode_parser()
    return computer.get_intcode()[0]

def search_input_for_desired_output(intcode, desired_output):
    computer = intcode_computer()
    for noun in range(100):
        for verb in range(100):
            computer.reset()
            computer.set_intcode(intcode)
            computer.set_alarm(noun, verb)
            computer.intcode_parser()
            if computer.get_intcode()[0] == desired_output:
                return 100 * noun + verb

if __name__ == '__main__':
    file = open('day2_input.txt', 'r')
    intcode = list(map(int, file.read().split(',')))

    desired_output = 19690720
    result = set_alarm_and_parse(intcode)
    result2 = search_input_for_desired_output(intcode, desired_output)

    print('Output of the IntCode = {}'.format(result))
    print('Input to the IntCode = {}'.format(result2))
