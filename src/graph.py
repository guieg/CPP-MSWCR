class Graph():

    def __init__(self) -> None:
        pass

    def __init__(self, nodes : list, edges: list) -> None:
        self.nodes = nodes
        self.edges = edges

    def get_degree(self, node):
        degree = 0
        for edge in self.edges:
            if node in edge[:2]:
                degree +=1
        return degree
    
    def add_node(self, node):
        pass

    def remove_node(self, node):
        pass

    def add_edge(self, edge):
        pass

    def remove_edge(self, edge):
        pass
