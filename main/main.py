from graph.graph_adjl import Graph
from graph.graph_adjl import Vertex

if __name__ == "__main__":

    graph = Graph()

    for i in range(ord('A'), ord('I')):
    # for i in range(0, 8):
        graph.add_vertex(Vertex(chr(i)))
        # graph.add_vertex(Vertex(str(i)))

    # edges = ['AB5', 'AE1', 'BF3', 'CG4', 'DE5', 'DH6', 'EH7', 'FG2', 'FI5', 'FJ9', 'GJ2', 'HI5']
    # edges = ['AB4', 'AC3', 'BD2', 'CB1', 'CD2', 'CE2', 'DF2', 'EF3']
    edges = []

    for edge in edges:
        graph.add_edge(edge[1:2], edge[:-2], edge[2:])

    print(graph)

    print(graph.i_dfs('A', 'F'))
    print(graph.r_dfs('A', 'F'))

    for p in graph.dfs_paths('A', 'F'):
        print(p)

    graph.dijkstra('A', 'F')

