
from src.main.graph.graph_adjl import Graph


def test():

    graph = Graph('Grafo 1')    # Cria o Grafo

    for i in range(ord('A'), ord('G') + 1):
        graph.add_vertex(chr(i))

    edges = ['AB5', 'AC8', 'AD4', 'BE7', 'CF10', 'DE5', 'DF11', 'EG9', 'FG6']

    for edge in edges:
        graph.add_edge(edge[0:1], edge[1:2], edge[2:])

    print(graph.name + ': \n')
    print(graph)

    print('O grafo possui {0} vértices e {1} arestas.'.format(
            len(list(graph.vertices)),
            len(list(graph.edges)))
          )

    print('Vertices: \n')
    print([v for v in graph.vertices])

    print('Arestas: \n')
    print([e for e in graph.edges])

    print('O grafo possui vértices isolados?')
    print('Sim' if len(graph.isolated_vertices) else 'Não')
    print('O grafo é conectado?')
    print('Sim' if graph.is_connected() else 'Não')
    print('O diâmetro do grafo é {}'.format(graph.diameter))
    print('A densidade do grafo é {}'.format(graph.density))
    print('O maior grau de vértice no grafo é {}.'.format(graph.max_degree))
    print('O menor grau de vértice no grafo é {}.'.format(graph.min_degree))
    print('Sequência de graus dos vértices:', graph.degree_sequence)
    print('O grafo tem uma sequência de graus não crescente?')
    print('Sim' if graph.is_degree_sequence(graph.degree_sequence) else 'Não')
    print('O grafo é simples?')
    print('Sim' if graph.erdoes_gallai(graph.degree_sequence) else 'Não')

    print('Depth-first Search')

    print(graph.i_dfs('A', 'G'))
    print(graph.r_dfs('A', 'G'))
    print([path for path in graph.dfs_paths('A', 'E')])

    print('Breadth-first Search')

    print(graph.i_bfs('A', 'G'))
    print(graph.r_bfs('A', 'G'))
    print([path for path in graph.bfs_paths('A', 'E')])

    print('Dijkstra')
    graph.dijkstra('A', 'G')

    print('Removendo o vértice D')
    graph.rm_vertex('D')
    print('O grafo agora tem {} vértices'.format(len(graph.keys())))
    print(graph)

    print('Removendo a aresta A --- B')
    graph.rm_edge('A', 'B')
    print('O grafo agora tem {} arestas'.format(len(list(graph.edges))))
    print(graph)

if __name__ == "__main__":
    test()



