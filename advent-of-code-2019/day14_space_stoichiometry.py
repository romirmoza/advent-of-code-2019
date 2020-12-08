import math
from collections import defaultdict

def req_met(req):
    for chem, quan in req.items():
        if chem != 'ORE' and quan > 0:
            return False
    return True

def run_reverse_reaction(chem, quan, reactions_dict, req):
    reaction = reactions_dict[chem]
    reactants = reaction[:-1]
    product = reaction[-1]
    coeff = math.ceil(quan/product[0])
    for reactant in reactants:
        req[reactant[1]] += coeff * reactant[0]
    req[product[1]] -= coeff * product[0]

def find_ore_req(reactions_dict, req):
    while not req_met(req):
        for chem, quan in req.items():
            if chem != 'ORE' and quan > 0:
                run_reverse_reaction(chem, quan, reactions_dict, req)
                break
    return 0

def max_fuel_possible(total_ore):
    N = 10000  # greater N => greater the accuracy of the ore_per_fuel estimate
    req = defaultdict(int)
    req['FUEL'] += N
    find_ore_req(reactions_dict, req)
    ore_per_fuel = req['ORE'] // N
    guess = int(total_ore // ore_per_fuel)

    while(1):
        req = defaultdict(int)
        req['FUEL'] += guess
        find_ore_req(reactions_dict, req)
        if req['ORE'] > total_ore:
            return guess - 1
        # print('ORE required = {:E}, Fuel made = {}'.format(req['ORE'], guess))
        guess += 1

if __name__ == '__main__':
    file = open('day14_input.txt', 'r')
    reactions = file.read().split('\n')[:-1]

    reactions_dict = {}
    for reaction in reactions:
        reaction = list(map(str.strip, reaction.replace(' =>', ',').split(',')))
        reaction = [(int(r.split()[0]), r.split()[1]) for r in reaction]
        reactions_dict[reaction[-1][1]] = reaction

    req = defaultdict(int)
    req['FUEL'] += 1
    find_ore_req(reactions_dict, req)

    total_ore = 1e+12
    max_fuel = max_fuel_possible(total_ore)

    print('ORE required for 1 fuel = {}'.format(req['ORE']))
    print('Max fuel possible from 1e+12 ORE = {}'.format(max_fuel))