import copy
from itertools import permutations
from intcode_computer import intcode_computer

# This is meant for the case where mutiple amps can be in the same phase
def get_phase_list(phase, num_amps, num_phases):
    phase_list = []
    for i in range(num_amps):
        phase_list.append(phase % num_phases)
        phase = phase // num_phases
    return phase_list

if __name__ == '__main__':
    inputampA = 0
    num_amps = 5
    num_phases = 5

    file = open('day7_input.txt', 'r')
    intcode_initial = list(map(int, file.read().split(',')))

    computer = [intcode_computer() for _ in range(num_amps)]
    max_output = 0
    for phase_list in permutations(range(num_phases)):
        outputamp = [inputampA for _ in range(num_amps)]
        for i in range(num_amps):
            intcode = copy.deepcopy(intcode_initial)
            computer[i].set_intcode(intcode)
            computer[i].set_input([phase_list[i], outputamp[i]])
            computer[i].intcode_parser()
            outputamp[(i+1) % num_amps] = int(computer[i].get_output())
        if outputamp[0] > max_output:
            max_output = outputamp[0]
            max_phase_list = phase_list
        [computer[i].reset() for i in range(num_amps)]

    print('Max thruster output = {}, for phase setting = {}'.format(max_output, max_phase_list))
