from collections import defaultdict

def setup(starting_numbers):
    memory = defaultdict(lambda: -1)
    for turn in range(len(starting_numbers)-1):
        num = starting_numbers[turn]
        memory[num] = turn + 1
    last_spoken = starting_numbers[-1]
    return memory, last_spoken

def memory_game(starting_numbers, n):
    memory, last_spoken = setup(starting_numbers)
    for turn in range(len(starting_numbers), n):
        mem_last = memory[last_spoken]
        if mem_last == -1:
            num = 0
        elif mem_last != -1:
            num = turn - mem_last
        memory[last_spoken] = turn
        last_spoken = num
        if not (turn + 1) % 1e6:
            print('Number spoken on turn {: >4} = {: >3}'.format(turn+1, num)) # '{message:{fill}{align}{width}}'.format()
    return last_spoken

if __name__ == '__main__':
    file = open('day15_input.txt', 'r')
    starting_numbers = list(map(int, file.read().split(',')))

    n, m = 2020, 30000000
    n_th = memory_game(starting_numbers, n)
    m_th = memory_game(starting_numbers, m)

    print('{}th number = {}'.format(n, n_th))
    print('{}th number = {}'.format(m, m_th))