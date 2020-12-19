import re

def rule_satisfies_every_field(rule, fields):
    for field in fields:
        flag = False
        for range in rule:
            if field >= range[0] and field <= range[1]:
                flag = True
                break
        if not flag:
            return False
    return True

def field_satisfies_any_rule(rules, field):
    for rule in rules.values():
        for range in rule:
            if field >= range[0] and field <= range[1]:
                return True
    return False

def ticket_scanning_error_rate(rules, ticket):
    error_rate = 0
    for field in ticket:
        if not field_satisfies_any_rule(rules, field):
            error_rate += field
    return error_rate

def ticket_scanning_error(rules, ticket):
    for field in ticket:
        if not field_satisfies_any_rule(rules, field):
            return True
    return False

def format_rules(rules):
    rules_dict = {}
    rules = rules.split('\n')
    for rule in rules:
        field = re.findall('^(.*):', rule)[0]
        ranges = re.findall('[0-9]*-[0-9]*', rule)
        ranges = [list(map(int, range.split('-'))) for range in ranges]
        rules_dict[field] = ranges
    return rules_dict

def product_departure_fields(field_identities, ticket):
    prod = 1
    for field_index, field_name in field_identities.items():
        if re.search('^departure', field_name):
            prod *= ticket[field_index]
    return prod

def identify_fields(rules, tickets):
    candidates_for_fields = []
    for index in range(len(tickets[0])):
        candidates_field_i = []
        fields = [ticket[index] for ticket in tickets]
        for rule_name, rule in rules.items():
            if rule_satisfies_every_field(rule, fields):
                candidates_field_i.append(rule_name)
        candidates_for_fields.append(candidates_field_i)

    field_identities = {}
    while 1:
        number_of_candidates = [[idx, len(rules)] for idx, rules in enumerate(candidates_for_fields) if len(rules) > 0]
        if not len(number_of_candidates):
            break
        min_candidate_index = min(number_of_candidates, key=lambda x: x[1])[0]
        min_candidate_length = min(number_of_candidates, key=lambda x: x[1])[1]
        field_identities[min_candidate_index] = candidates_for_fields[min_candidate_index][0]

        for candidate in candidates_for_fields:
            if field_identities[min_candidate_index] in candidate:
                candidate.remove(field_identities[min_candidate_index])
    return field_identities

if __name__ == '__main__':
    file = open('day16_input.txt', 'r')
    rules, my_ticket, nearby_tickets = list(file.read().split('\n\n'))

    rules = format_rules(rules)
    my_ticket = list(map(int, my_ticket.split('\n')[1].split(',')))
    nearby_tickets = nearby_tickets.split('\n')[1:]
    nearby_tickets = [list(map(int, ticket.split(','))) for ticket in nearby_tickets]

    error_rate = sum([ticket_scanning_error_rate(rules, ticket) for ticket in nearby_tickets])
    nearby_tickets_valid = filter(lambda ticket: not ticket_scanning_error(rules, ticket), nearby_tickets)

    field_identities = identify_fields(rules, nearby_tickets_valid)
    prod = product_departure_fields(field_identities, my_ticket)

    print('Ticket scanning error rate = {}'.format(error_rate))
    print('Product of the six departure fields = {}'.format(prod))
