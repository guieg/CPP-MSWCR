class ChinesePostmanProblem():
    def __init__(self, graph) -> None:
        self.graph = graph

    def dijkstra(self):
        pass

    def get_cycle(self):
        # Cria um dicionário para armazenar os vizinhos de cada vértice
        adj_list = {}
        for node in self.graph.nodes:
            adj_list[node] = []

        for u, v in self.graph.edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        # Inicializa a pilha e a lista de vértices visitados
        start = None
        for node in self.graph.nodes:
            for edge in self.graph.edges:
                if node in edge:
                    start = node
                    break
            
        stack = [start]
        cycle = []

        while stack:
            u = stack[-1]

            if len(adj_list[u]) == 0:
                # Se não houver mais vizinhos não visitados para o vértice atual,
                # adiciona o vértice à lista do ciclo euleriano
                cycle.append(u)
                stack.pop()
            else:
                # Caso contrário, escolhe um vizinho não visitado do vértice atual
                v = adj_list[u][0]
                # Remove a aresta entre u e v
                adj_list[u].remove(v)
                adj_list[v].remove(u)
                try:
                    self.graph.edges.remove([u,v])
                except:
                    self.graph.edges.remove([v,u])
                # Adiciona o vizinho v à pilha
                stack.append(v)

        # Retorna a lista do ciclo euleriano (invertida)
        return cycle[::-1]

    def hierholzer(self):
        for edge in self.graph.edges:
            edge.pop()
        eulerian_path = []
        while True:
            try:
                eulerian_path += self.get_cycle()
            except:
                break
        return eulerian_path

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
            print("Caminho euleriano: " + str(self.hierholzer()))
            
        else:
            print("Não é euleriano")
            #self.find_best_minimum_pairing()