import networkx as nx

if __name__ == '__main__':
    file = open('day6_input.txt', 'r')
    edges = file.read().split()
    G = nx.Graph()
    for e in edges:
        u = e.split(')')[0]
        v = e.split(')')[1]
        G.add_edge(u, v)

    source = 'YOU'
    target = 'SAN'
    path_length = len(nx.shortest_path(G, source, target)) - 3 
    print('Number of transfers = {}'.format(path_length))
