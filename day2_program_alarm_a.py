from intcode_computer import intcode_computer

if __name__ == '__main__':
    file = open('day2_input.txt', 'r')
    intcode = list(map(int, file.read().split(',')))

    computer = intcode_computer(intcode)
    computer.set_alarm1202()
    computer.intcode_parser()
    print('Output of the IntCode = {}'.format(computer.get_intcode()[0]))
