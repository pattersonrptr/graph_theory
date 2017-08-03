
from src.main.graph.graph_adjl import Graph, Vertex


def test():

    graph = Graph('Grafo 1', is_directed=True)    # Cria o Grafo

    for i in range(ord('A'), ord('G') + 1):
        graph.add_vertex(chr(i))

    edges = ['AB5', 'AC8', 'AD4', 'BE7', 'CF10', 'DE5', 'DF11', 'EG9', 'FG6']

    for edge in edges:
        graph.add_edge(edge[0:1], edge[1:2], int(edge[2:]))

    graph.add_vertex('H')
    graph.add_vertex('I')
    graph.add_edge('H', 'H', 0)

    print(graph.name + ': \n')
    print(graph)

    print([(v, graph.degree(v)) for v in graph.vertices])

    print(graph.min_degree)
    print(graph.max_degree)

    print(graph.degree_sequence)

    print('Isolados:', graph.isolated_vertices)

if __name__ == "__main__":
    test()



