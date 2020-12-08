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

def phase_for_max_output(input_to_ampA, num_amps, num_phases):
    computer = [intcode_computer() for _ in range(num_amps)]
    max_output = 0
    for phase_list in permutations(range(num_phases)):
        output_amp = [input_to_ampA for _ in range(num_amps)]
        for i in range(num_amps):
            computer[i].set_intcode(intcode)
            computer[i].set_input([phase_list[i], output_amp[i]])
            computer[i].intcode_parser()
            output_amp[(i+1) % num_amps] = int(computer[i].get_output())
        if output_amp[0] > max_output:
            max_output = output_amp[0]
            max_phase_list = phase_list
        [computer[i].reset() for i in range(num_amps)]
    return max_output, max_phase_list


def phase_for_max_output_feedback_loop(input_to_ampA, num_amps, num_phases):
    computer = [intcode_computer() for _ in range(num_amps)]
    max_output = 0
    for phase_list in permutations(range(num_amps, num_amps + num_phases)):
        output_amp = [input_to_ampA for _ in range(num_amps)]
        [computer[i].set_intcode(intcode) for i in range(num_amps)]
        [computer[i].set_input([phase_list[i]]) for i in range(num_amps)]
        j = 0
        while not all([computer[i].has_halted() for i in range(num_amps)]):
            i = j % num_amps
            computer[i].extend_input([output_amp[i]])
            computer[i].intcode_parse_until_output()
            if computer[i].get_output():
                output_amp[(i+1) % num_amps] = int(computer[i].get_output())
                computer[i].clear_output()
            j += 1
        if output_amp[0] > max_output:
            max_output = output_amp[0]
            max_phase_list = phase_list
        [computer[i].reset() for i in range(num_amps)]
    return max_output, max_phase_list

if __name__ == '__main__':
    input_to_ampA, num_amps, num_phases = 0, 5, 5
    file = open('day7_input.txt', 'r')
    intcode = list(map(int, file.read().split(',')))

    # part a
    max_output, max_phase_list = phase_for_max_output(input_to_ampA, num_amps, num_phases)
    print('Max thruster output = {}, for phase setting = {}'.format(max_output, max_phase_list))

    # part b
    max_output, max_phase_list = phase_for_max_output_feedback_loop(input_to_ampA, num_amps, num_phases)
    print('Max thruster output = {}, for phase setting = {}'.format(max_output, max_phase_list))
