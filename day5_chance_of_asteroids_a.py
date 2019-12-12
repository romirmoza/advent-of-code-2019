from intcode_computer import intcode_computer

if __name__ == '__main__':
    file = open('day5_input.txt', 'r')
    intcode = map(int, file.read().split(','))

    computer = intcode_computer(intcode)
    computer.intcode_parser()
    print('Output of the IntCode = {}'.format(computer.get_output()))
