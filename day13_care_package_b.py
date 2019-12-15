from intcode_computer import intcode_computer

def relative_position(p, q):
    if p > q:
        return -1
    elif p < q:
        return 1
    else:
        return 0

if __name__ == '__main__':
    file = open('day13_input.txt', 'r')
    intcode = list(map(int, file.read().split(',')))

    intcode[0] = 2      # play for free!!
    blocks = 0
    computer = intcode_computer(intcode, [0])
    while 1:
        computer.intcode_parse_until_output()
        computer.intcode_parse_until_output()
        computer.intcode_parse_until_output()
        if computer.has_halted():
            break
        x, y, id = list(map(int, computer.get_output().split()))
        if x == -1 and y == 0:
            print('Current score = {}'.format(id))
        if id == 3:
            paddle = x
        if id == 4:
            ball = x
            if 'paddle' in locals():
                computer.extend_input([relative_position(paddle, ball)])
        computer.clear_output()
