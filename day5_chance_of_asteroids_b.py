from intcode_computer import intcode_computer

if __name__ == '__main__':
    file = open('day5_input.txt', 'r')
    intcode = list(map(int, file.read().split(',')))

    id = 5
    computer = intcode_computer(intcode, id)
    computer.intcode_parser()
    print('Output of the IntCode = {}'.format(computer.get_output()))
