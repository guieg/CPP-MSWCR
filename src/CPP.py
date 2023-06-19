from sys import maxsize

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

    def get_cycle(self):

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

    def hierholzer(self):
        for edge in self.graph.edges:
            edge.pop()
        return self.get_cycle()

    def gen_pairs(self,odds):
        pairs = []
        for i in range(len(odds)-1):
            pairs.append([])
            for j in range(i+1,len(odds)):
                pairs[i].append([odds[i],odds[j]])
        return pairs

        
    def get_pairs(self, pairs, l, done = [], final = [], pairings_sum = []):
        if(pairs[0][0][0] not in done):
            done.append(pairs[0][0][0])
            for i in pairs[0]:
                f = final[:]
                val = done[:]
                if(i[1] not in val):
                    f.append(i)
                else:
                    continue
                if(len(f)==l):
                    pairings_sum.append(f)
                    return 
                else:
                    val.append(i[1])
                    self.get_pairs(pairs[1:], l,val, f, pairings_sum)
                    
                    
        else:
            self.get_pairs(pairs[1:], l, done, final, pairings_sum)
        return pairings_sum
            
        
    def check_eulerian(self):
        odd_nodes = [n for n in self.graph.get_nodes() if self.graph.get_degree(n) % 2 != 0]
        if len(odd_nodes) == 0:
            return True
        return False

    def find_best_minimum_pairing(self):
        odd_nodes = [n for n in self.graph.get_nodes() if self.graph.get_degree(n) % 2 != 0]
        print(odd_nodes)
        initial_pairs = self.gen_pairs(odd_nodes)
        print('initial pairs are:',initial_pairs)
        if(len(initial_pairs) > 4):
            l = (len(initial_pairs)+1)//2
            complete_pairs = self.get_pairs(initial_pairs,l)
            print('complete pairs are :',complete_pairs)
            print('number of combinations', len(complete_pairs))
        else:
            complete_pairs = initial_pairs
            print('complete pairs are :',complete_pairs)
            print('number of combinations', len(complete_pairs))
        return complete_pairs

    def solve_cpp(self):
        if self.check_eulerian():
            print("É euleriano")
            print("Caminho euleriano: " + str(self.hierholzer()))
            
        else:
            print("Não é euleriano")
            pairs_sets = self.find_best_minimum_pairing()

            for set in pairs_sets:
                for pair in set:
                    u, v = pair
                    print(u, v)
                    print("Distance " + str(u) + " to " + str(v)+": " + str(self.dijkstra(pair)))