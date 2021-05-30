from collections import defaultdict


class Graph:
    # Método construtor
    def __init__(self):
        self.vertices = []  # Vertices
        self.edges = defaultdict(list)  # Arestas
        self.weights = {}  # Pesos

    # Adiciona vértice
    def add_vertex(self, value):
        self.vertices.append(value)
        self.edges[value] = []

    # Ediciona aresta
    def add_edge(self, origin, destination, weight):
        # Caso origem não esteja nos vértices adiciona
        if origin not in self.vertices:
            self.add_vertex(origin)

        # Caso destino não esteja nos vértices adiciona
        if destination not in self.vertices:
            self.add_vertex(destination)

        # Adiciona dict com chave como origem e valor como destino
        self.edges[origin].append(destination)

        # Adiciona peso da aresta (origem, destino)
        self.weights[(origin, destination)] = weight
        self.weights[(destination, origin)] = weight
