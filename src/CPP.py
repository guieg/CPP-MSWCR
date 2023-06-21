from sys import maxsize
from itertools import combinations

class ChinesePostmanProblem():
    def __init__(self, graph) -> None:
        self.graph = graph

    def dijkstra(self, pair):
        ad_list = {}
        for node in self.graph.get_nodes():
            ad_list[node] = []

        for u, v, p in self.graph.get_edges():
            ad_list[u].append([v, p])
            ad_list[v].append([u, p])

        start, end = pair
        nodes = self.graph.get_nodes()
        unvisited = nodes.copy()

        path_costs = {}
        previous_nodes = {}
        for node in nodes:
            path_costs[node] = maxsize
            previous_nodes[node] = None
        path_costs[start] = 0

        

        node = start
        while unvisited:
            for ad in ad_list[node]:
                next_node = ad[0]

                if next_node not in unvisited:
                    continue
                
                if path_costs[next_node] > path_costs[node] + ad[1]:
                    path_costs[next_node] = path_costs[node] + ad[1]
                    previous_nodes[next_node] = node

            unvisited.remove(node)
            
            ads = {}
            for u, v in path_costs.items():
                if u in unvisited:
                    ads[u] = v
            
            if len(ads) > 0:
                node = min(ads, key=ads.get) 
            else:
                break

            if node == end:
                break

        cost = path_costs[end]

        path = []
        previous = end
        while previous != None:
            path.insert(0, previous)
            previous = previous_nodes[previous]

        return cost, path

    def hierholzer(self):
        ad_list = {}

        for node in self.graph.nodes:
            ad_list[node] = []

        for u, v in self.graph.edges:
            ad_list[u].append(v)
            ad_list[v].append(u)

        start = None
        for node in self.graph.nodes:
            for edge in self.graph.edges:
                if node in edge:
                    start = node
                    break
            
        stack, cycle = [start], []

        while stack:
            i = stack[-1]

            if len(ad_list[i]) == 0:
                cycle.append(i)
                stack.pop()
            else:
                j = ad_list[i][0]
                ad_list[i].remove(j)
                ad_list[j].remove(i)
                stack.append(j)

        return cycle[::-1]
   
    def check_eulerian(self):
        odd_nodes = [n for n in self.graph.get_nodes() if self.graph.get_degree(n) % 2 != 0]
        if len(odd_nodes) == 0:
            return True
        return False
    
    def get_possible_sets(self):
        odd_nodes = [n for n in self.graph.get_nodes() if self.graph.get_degree(n) % 2 != 0]
        all_pairs = list(combinations(odd_nodes, 2))
        list_of_sets = []
        for x, y in all_pairs:
            new_set = [[x, y]]
            for a, b in all_pairs:
                isIn = False
                for pair in new_set:
                    if a in pair or b in pair:
                        isIn = True
                        break
                        
                if not isIn:
                    new_set.append([a, b])
            reverse = new_set.copy()
            reverse.reverse()
            if reverse not in list_of_sets:
                list_of_sets.append(new_set)
        return list_of_sets
    


    def solve_cpp(self):
        cost = self.graph.get_cost()
        if self.check_eulerian():
            print("É euleriano")
            
            for edge in self.graph.edges:
                edge.pop()
            print("Caminho euleriano: " + str(self.hierholzer()))
            
        else:
            print("Não é euleriano")
            pairs_sets = self.get_possible_sets()
            print(pairs_sets)

            set_sums = {}
            pair_path = {}
            for set in range(len(pairs_sets)):
                set_sums[set] = 0
                for pair in range(len(pairs_sets[set])):
                    u, v = pairs_sets[set][pair]
                    distance, path = self.dijkstra((u, v))
                    set_sums[set] += distance
                    pair_path[pair] = path

            minimum_set = min(set_sums, key=set_sums.get)
            chosed_set = pairs_sets[minimum_set]
            cost += set_sums[minimum_set]
            for edge in self.graph.edges:
                edge.pop()

            print(chosed_set)
            for pair in range(len(chosed_set)):
                    for node in range(len(pair_path[pair])-1):
                        if [pair_path[pair][node], pair_path[pair][node+1]] in self.graph.edges:
                            self.graph.edges.append([pair_path[pair][node], pair_path[pair][node+1]])
                        else:
                            self.graph.edges.append([pair_path[pair][node+1], pair_path[pair][node]])
            #print(self.graph.edges)
            print("Caminho euleriano: " + str(self.hierholzer()))
        print("Custo:" + str(cost))