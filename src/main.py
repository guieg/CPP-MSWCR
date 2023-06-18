from sys import argv
from CPP import ChinesePostmanProblem
from graph import Graph
import networkx as nx
import matplotlib.pyplot as plt
from copy import deepcopy

def read_file_to_graph(path):
    file = open(path, 'r')
    lines = [line.rstrip() for line in file]
    file.close()
    nodes = [int(element) for element in lines[:lines.index('#')]]
    edges = [ [ int(e) for e in element.split(' ')] for element in lines[lines.index('#') +1 :]]
    return Graph(nodes, edges)

def plot(graph : Graph):
    G = nx.Graph()
    G.add_nodes_from(graph.get_nodes())
    G.add_weighted_edges_from(graph.get_edges())

    pos = nx.spring_layout(G, seed=7)

    nx.draw_networkx_nodes(G, pos, node_size=100)

    nx.draw_networkx_edges(G, pos, edgelist=G.edges(data=True), width=2)

    nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif")

    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels)

    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    graphs = [read_file_to_graph(file_path) for file_path in argv[1:]]
    for graph in graphs:
        g = deepcopy(graph)
        CPP = ChinesePostmanProblem(graph)
        CPP.solve_cpp()
        plot(g)