from intcode_computer import intcode_computer

if __name__ == '__main__':
    file = open('day13_input.txt', 'r')
    intcode = list(map(int, file.read().split(',')))

    blocks = 0
    computer = intcode_computer(intcode)
    while 1:
        computer.intcode_parse_until_output()
        computer.intcode_parse_until_output()
        computer.intcode_parse_until_output()
        if computer.has_halted():
            break
        x, y, id = list(map(int, computer.get_output().split()))
        if id == 2:
            blocks += 1
        computer.clear_output()

    print('Number of block tiles = {}'.format(blocks))
