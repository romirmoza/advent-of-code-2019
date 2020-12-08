from intcode_computer import intcode_computer

def count_blocks_arcade_game(intcode):
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
    return blocks

def relative_position(p, q):
    if p > q:
        return -1
    elif p < q:
        return 1
    else:
        return 0

def run_arcade_game(intcode):
    computer = intcode_computer(intcode, [0])
    while 1:
        for i in range(3): computer.intcode_parse_until_output()
        if computer.has_halted():
            return score
            break
        x, y, id = list(map(int, computer.get_output().split()))
        if x == -1 and y == 0:
            score = id
        if id == 3:
            paddle = x
        if id == 4:
            ball = x
            if 'paddle' in locals():
                computer.extend_input([relative_position(paddle, ball)])
        computer.clear_output()
    return

if __name__ == '__main__':
    file = open('day13_input.txt', 'r')
    intcode = list(map(int, file.read().split(',')))

    blocks = count_blocks_arcade_game(intcode)

    intcode[0] = 2      # play for free!!
    final_score = run_arcade_game(intcode)

    print('Number of block tiles = {}'.format(blocks))
    print('Final score = {}'.format(final_score))
