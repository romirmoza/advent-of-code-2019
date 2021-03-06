import networkx as nx

def count_orbits(G):
    count = 0
    for node in G.nodes:
        count += len(list(nx.edge_dfs(G, node, orientation='reverse')))
    return count

def build_graph(edges):
    G = nx.DiGraph()
    for e in edges:
        u = e.split(')')[0]
        v = e.split(')')[1]
        G.add_edge(u, v)
    return G

if __name__ == '__main__':
    file = open('day6_input.txt', 'r')
    edges = file.read().split()
    G = build_graph(edges)

    # part a
    count = count_orbits(G)
    print('Sum of orbits = {}'.format(count))

    # part b
    source = 'YOU'
    target = 'SAN'
    G = G.to_undirected()
    path_length = len(nx.shortest_path(G, source, target)) - 3
    print('Number of transfers = {}'.format(path_length))
