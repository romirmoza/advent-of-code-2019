from intcode_computer import intcode_computer

if __name__ == '__main__':
    file = open('day9_input.txt', 'r')
    intcode = list(map(int, file.read().split(',')))

    test_mode = [1]
    computer = intcode_computer(intcode, test_mode)
    computer.intcode_parser()
    output_test_mode = computer.get_output()

    boost_mode = [2]
    computer = intcode_computer(intcode, boost_mode)
    computer.intcode_parser()
    output_boost_mode = computer.get_output()

    print('Output of the IntCode in test mode= {}'.format(output_test_mode))
    print('Output of the IntCode in boost mode = {}'.format(output_boost_mode))


