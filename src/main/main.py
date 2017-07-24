
from src.main.graph.graph_adjl import Graph


def test():

    graph = Graph('Grafo 1', is_directed=False)    # Cria o Grafo

    for i in range(ord('A'), ord('G') + 1):
        graph.add_vertex(chr(i))

    edges = ['AB5', 'AC8', 'AD4', 'BE7', 'CF10', 'DE5', 'DF11', 'EG9', 'FG6']

    for edge in edges:
        graph.add_edge(edge[0:1], edge[1:2], int(edge[2:]))

    print(graph.name + ': \n')
    print(graph)

    print('Adicinando uma aresta de D para D (loop)')
    graph.add_edge('D', 'D', 3)

    print('Adicionando vértice isolado H')
    graph.add_vertex('H')

    print('O grafo possui {0} vértices e {1} arestas.'.format(
            len(list(graph.vertices)),
            len(list(graph.edges)))
          )

    print('Vertices: \n')
    print([v for v in graph.vertices])

    print('Arestas: \n')
    print([e for e in graph.edges])

    print('O grafo possui vértices isolados?')
    print(graph.isolated_vertices)
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
    print([path for path in graph.dfs_paths('A', 'G')])

    print('Breadth-first Search')

    print(graph.i_bfs('A', 'G'))
    print(graph.r_bfs('A', 'G'))
    print([path for path in graph.bfs_paths('A', 'G')])

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

    print('Adicionando nova conexão de A para B')
    graph.add_edge('A', 'B', 5)
    print(graph)

    print('Adicionando mais uma conexão de A para B')
    graph.add_edge('A', 'B', 3)

    print('Adicionando uma conexão de C para B')
    graph.add_edge('C', 'B', 3)

    print('Adicionando outra conexão de C para B')
    graph.add_edge('C', 'B', 4)

    print('Adicionando uma conexão de B para D')
    print('Adicionado com sucesso!' if graph.add_edge('B', 'D', 2) else 'Não funciona porque o D foi deletado!')

    print(graph)

    graph.dijkstra('A', 'G')

if __name__ == "__main__":
    test()



