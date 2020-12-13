from collections import defaultdict

def count_arrangements(jolt_list):
    if len(jolt_list) <= 2:
        return 1

    for i in range(1, len(jolt_list)-1):
        if jolt_list[i] - jolt_list[i-1] == 3:
            return count_arrangements(jolt_list[:i]) * count_arrangements(jolt_list[i:])

    if jolt_list[2] - jolt_list[0] > 3:
        return count_arrangements(jolt_list[1:])

    if jolt_list[2] - jolt_list[0] <= 3:
        return count_arrangements(jolt_list[:1] + jolt_list[2:]) + count_arrangements(jolt_list[1:])


def count_diffs(jolt_list):
    diffs = defaultdict(int)
    for i in range(1, len(jolt_list)):
        diffs[jolt_list[i]-jolt_list[i-1]] += 1
    return diffs

if __name__ == '__main__':
    file = open('day10_input.txt', 'r')
    jolt_list = list(map(int,file.read().split('\n')))

    jolt_list.sort()
    jolt_list.insert(0, 0)
    jolt_list.append(jolt_list[-1]+3)

    diffs = count_diffs(jolt_list)
    arrangements = count_arrangements(jolt_list)

    print('Number of 1-jolt differences multiplied by the number of 3-jolt differences = {}'.format(diffs[1]*diffs[3]))
    print('Number of arrangements = {}'.format(arrangements))