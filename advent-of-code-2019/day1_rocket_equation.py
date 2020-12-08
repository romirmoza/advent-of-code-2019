def calculate_fuel_req(module):
    return (module // 3) - 2

def calculate_fuel_req_recursive(module):
    req = (module // 3) - 2
    if req > 0:
        return req + calculate_fuel_req_recursive(req)
    return 0

if __name__ == '__main__':
    file = open('day1_input.txt', 'r')
    modules = list(map(int, file.read().split()))
    reqa = sum([calculate_fuel_req(mod) for mod in modules])

    reqb = sum([calculate_fuel_req_recursive(mod) for mod in modules])

    print('Total fuel required = {}'.format(reqa))
    print('Total fuel required recursive = {}'.format(reqb))
