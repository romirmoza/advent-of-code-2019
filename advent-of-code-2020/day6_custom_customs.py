def count_yes_anyone_in_group(answers):
    return len(set(list(answers.replace('\n', ''))))

def count_yes_everyone_in_group(answers):
    return len(set.intersection(*map(set, answers.split('\n'))))

if __name__ == '__main__':
    file = open('day6_input.txt', 'r')
    groups = list(file.read().split('\n\n'))

    count_any, count_every = 0, 0
    for answers in groups:
        count_any += count_yes_anyone_in_group(answers)
        count_every += count_yes_everyone_in_group(answers)

    print('Count of questions to which anyone answered "yes" = {}'.format(count_any))
    print('Count of questions to which everyone answered "yes" = {}'.format(count_every))
