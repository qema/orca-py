import orca
import networkx as nx

print(orca.orbit_counts("node", 5, nx.gnm_random_graph(30, 100)))
