import networkx as nx
import re
from collections import defaultdict

def rules_to_digraph(rules):
    G = nx.DiGraph()
    for rule in rules:
        u = re.findall('^(.*) bags contain', rule)[0]
        v_list = re.findall('([0-9]) (.*?) bag', rule)
        for v in v_list:
            G.add_edge(u, v[1], weight=int(v[0]))
    return G

def count_bags(digraph, source, count_bags_dict):
    children = [x[1] for x in  digraph.edges(source)]
    if not children:
        count_bags_dict[source] = 1
        return count_bags_dict[source]
    count = 0
    for child in children:
        if count_bags_dict[child]:
            count += digraph.edges[source, child]['weight'] * count_bags_dict[child]
        else:
            count += digraph.edges[source, child]['weight'] * count_bags(digraph, child, count_bags_dict)
    count_bags_dict[source] = count + 1
    return count_bags_dict[source]

if __name__ == '__main__':
    file = open('day7_input.txt', 'r')
    rules = list(file.read().split('\n'))

    digraph = rules_to_digraph(rules)
    count_ancestors = len(nx.ancestors(digraph, source='shiny gold'))

    count_bags_dict = defaultdict(int)
    count_bags = count_bags(digraph, 'shiny gold', count_bags_dict) - 1

    print('Number of ancestors to "shiny gold" = {}'.format(count_ancestors))
    print('Number of bags in "shiny gold" = {}'.format(count_bags))

