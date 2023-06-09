from sys import argv
from pandas import read_csv
from graph import Graph

def chinese_postman_problem_solver():
    pass

def read_file_to_graph(path):
    file = open(path, 'r')
    lines = [line.rstrip() for line in file]
    file.close()
    nodes = [int(element) for element in lines[:lines.index('#')]]
    edges = [ [ int(e) for e in element.split(' ')] for element in lines[lines.index('#') +1 :]]
    return Graph(nodes, edges)

if __name__ == "__main__":
    graphs = [read_file_to_graph(file_path) for file_path in argv[1:]]
    for graph in graphs:
        print(graph.get_degree(2))

    pass
    chinese_postman_problem_solver()