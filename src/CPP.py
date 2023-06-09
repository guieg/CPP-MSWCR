class ChinesePostmanProblem():
    def __init__(self, graph) -> None:
        self.graph = graph

    def dijkstra(self):
        pass

    def hierholzer(self):
        pass

    def check_eulerian(self):
        odd_nodes = [n for n in self.graph.get_nodes() if self.graph.get_degree(n) % 2 != 0]
        if len(odd_nodes) == 0:
            return True
        print(odd_nodes)
        return False

    def find_best_minimum_pairing(self):
        pass

    def solve_cpp(self):
        if self.check_eulerian():
            print("É euleriano")
        else:
            print("Não é euleriano")