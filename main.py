from models.network import Network
from models.graph import Graph
from models.network import Network


def main():
    # Inicia grafo e adiciona arestas
    graph = Graph()
    graph.add_edge("s", "a", 15)
    graph.add_edge("a", "c", 12)
    graph.add_edge("c", "t", 7)
    graph.add_edge("c", "b", 3)
    graph.add_edge("s", "b", 4)
    graph.add_edge("b", "d", 10)
    graph.add_edge("d", "t", 10)
    graph.add_edge("d", "a", 5)

    # Recebe resultado equivalente ao fluxo máximo no grafo
    network = Network(graph, 's', 't')
    print("Max network flow: ", network.ford_fulkerson())


if __name__ == '__main__':
    main()
