import copy
from itertools import permutations
from intcode_computer import intcode_computer

if __name__ == '__main__':
    inputampA = 0
    num_amps = 5
    num_phases = 5

    file = open('day7_input.txt', 'r')
    intcode_initial = list(map(int, file.read().split(',')))

    computer = [intcode_computer() for _ in range(num_amps)]
    max_output = 0
    for phase_list in permutations(range(num_amps, num_amps + num_phases)):
        outputamp = [inputampA for _ in range(num_amps)]
        intcode = [copy.deepcopy(intcode_initial) for _ in range(num_amps)]
        [computer[i].set_intcode(intcode[i]) for i in range(num_amps)]
        [computer[i].set_input([phase_list[i]]) for i in range(num_amps)]
        j = 0
        while not all([computer[i].has_halted() for i in range(num_amps)]):
            i = j % num_amps
            computer[i].extend_input([outputamp[i]])
            computer[i].intcode_parse_until_output()
            if computer[i].get_output():
                outputamp[(i+1) % num_amps] = int(computer[i].get_output())
                computer[i].clear_output()
            j += 1
        if outputamp[0] > max_output:
            max_output = outputamp[0]
            max_phase_list = phase_list
        [computer[i].reset() for i in range(num_amps)]

    print('Max thruster output = {}, for phase setting = {}'.format(max_output, max_phase_list))
