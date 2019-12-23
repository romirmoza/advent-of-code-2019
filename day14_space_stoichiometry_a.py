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
    print('ORE required = {}'.format(req['ORE']))
