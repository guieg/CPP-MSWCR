class ChinesePostmanProblem():
    def __init__(self, graph) -> None:
        self.graph = graph

    def dijkstra(self):
        pass

    def hierholzer(self):
        pass

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
        print(odd_nodes)
        return False

    def find_best_minimum_pairing(self):
        odd_nodes = [n for n in self.graph.get_nodes() if self.graph.get_degree(n) % 2 != 0]
        initial_pairs = self.gen_pairs(odd_nodes)
        print('initial pairs are:',initial_pairs)
        l = (len(initial_pairs)+1)//2
        complete_pairs = self.get_pairs(initial_pairs,l)
        print('complete pairs are :',complete_pairs)
        print('number of combinations', len(complete_pairs))

    def solve_cpp(self):
        if self.check_eulerian():
            print("É euleriano")
            
        else:
            print("Não é euleriano")
            self.find_best_minimum_pairing()