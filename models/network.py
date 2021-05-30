from models.graph import Graph


class Network:
    def __init__(self, graph, source, sink):
        self.graph = graph #grafo
        self.source = source #origem
        self.sink = sink #ralo
        self.max_flow = 0 #fluxo máximo
        self.visited = [] #vértices visitados
        self.parent = [] #pais dos vértices visitados

    def bfs(self):
        #Inicializa visitados, pais e fila como um array vazio
        self.visited = []
        self.parent = []
        queue = []

        #Adiciona a origem aos vetores e None como pai da origem
        queue.append(self.source)
        self.visited.append(self.source)
        self.parent.append(None)

        #Enquanto a fila não estiver vazia
        while len(queue) > 0:
            #Retira primeiro elemento da fila
            u = queue.pop(0)

            #Para todos os vértices conectados ao "u"
            for i in self.graph.edges[u]:
                #Caso o vértice filho não tenha sido visitado e o fluxo não estourou sua capacidade
                if self.graph.weights[(u, i)] > 0 and i not in self.visited:
                    queue.append(i)
                    self.visited.append(i)
                    self.parent.append(u)

        #Caso o ralo esteja dentro do visitados, indica caminho portando retorna verdadeiro
        if self.sink in self.visited:
            return True

        return False

    def ford_fulkerson(self):
        #Enquanto houver caminho
        while self.bfs():
            #Inicia capacidade minima do caminho com infinito para que a condição seja aceita na primeira iteração
            min_capacity = float('inf')

            #Inicia "v" como o ralo, realizando o caminho inverso, do ralo até origem
            v = self.sink

            #Define a capacidade mínima dentro do caminho
            while not v == self.source:
                u = self.parent[self.visited.index(v)]
                min_capacity = min(min_capacity, self.graph.weights[(u, v)])
                v = u

            v = self.sink

            #Atualiza o grafo com os novos valores de fluxo
            while not v == self.source:
                u = self.parent[self.visited.index(v)]
                self.graph.weights[(u, v)] -= min_capacity
                self.graph.weights[(v, u)] += min_capacity
                v = u

            #A capacidade mínima do caminho é somada à capacidade máxima
            self.max_flow += min_capacity

        return self.max_flow
