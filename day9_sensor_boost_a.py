from intcode_computer import intcode_computer

if __name__ == '__main__':
    file = open('day9_input.txt', 'r')
    intcode = list(map(int, file.read().split(',')))

    test_mode = [1]
    computer = intcode_computer(intcode, test_mode)
    computer.intcode_parser()
    print('Output of the IntCode = {}'.format(computer.get_output()))
