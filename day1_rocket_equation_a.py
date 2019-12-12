def calculate_fuel_req(module):
    return (module // 3) - 2

if __name__ == '__main__':
    file = open('day1_input.txt', 'r')
    modules = list(map(int, file.read().split()))
    req = sum([calculate_fuel_req(mod) for mod in modules])

    print('Total fuel required = {}'.format(req))
