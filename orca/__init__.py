import orcastr
import networkx as nx

def orbit_counts(task, size, graph):
    graph = nx.convert_node_labels_to_integers(graph)
    s = "{} {}\n".format(len(graph), len(graph.edges))
    for u, v in graph.edges:
        if u == v: continue
        s += "{} {}\n".format(u, v)
    out = orcastr.motif_counts_str(task, size, s)
    out = [[int(c) for c in s.split(" ")] for s in out.split("\n") if s]
    return out

