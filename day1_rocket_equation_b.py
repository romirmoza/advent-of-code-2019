def calculate_fuel_req_recursive(module):
    req = (module // 3) - 2
    if req > 0:
        return req + calculate_fuel_req_recursive(req)
    return 0

if __name__ == '__main__':
    file = open('day1_input.txt', 'r')
    modules = map(int, file.read().split())
    req = sum([calculate_fuel_req_recursive(mod) for mod in modules])

    print('Total fuel required = {}'.format(req))
