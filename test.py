import orca
import networkx as nx

counts = orca.orbit_counts("node", 5, nx.gnm_random_graph(30, 100))
print(f'Number of nodes: {len(counts)}')
print(f'Number of graphlets: {len(counts[0])}')
print('Counts: ', counts)
