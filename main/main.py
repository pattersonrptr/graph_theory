from graph.graph_adjl import Graph
from graph.graph_adjl import Vertex


def testa_dijkstra():
    graph = Graph()

    for i in range(ord('A'), ord('E')):
        # for i in range(0, 8):
        graph.add_vertex(Vertex(chr(i)))
        # graph.add_vertex(Vertex(str(i)))

    # edges = ['AB5', 'AE1', 'BF3', 'CG4', 'DE5', 'DH6', 'EH7', 'FG2', 'FI5', 'FJ9', 'GJ2', 'HI5']
    # edges = ['AB4', 'AC3', 'BD2', 'CB1', 'CD2', 'CE2', 'DF2', 'EF3']
    edges = ['AB8', 'AC7', 'BC7', 'CD6', 'BD3']

    for edge in edges:
        graph.add_edge(edge[1:2], edge[:-2], edge[2:])

    print(graph)

    print(graph.i_dfs('A', 'D'))
    print(graph.r_dfs('A', 'D'))

    for p in graph.dfs_paths('A', 'D'):
        print(p)

    graph.dijkstra('A', 'D')


def testa():

    g = Graph()

    for i in range(8):
        g.add_vertex(Vertex(i))

    g.add_edge('0', '2')
    g.add_edge('2', '0')
    g.add_edge('0', '7')
    g.add_edge('7', '0')
    g.add_edge('2', '6')
    g.add_edge('6', '2')
    g.add_edge('6', '4')
    g.add_edge('4', '6')
    g.add_edge('5', '3')
    g.add_edge('5', '4')
    g.add_edge('4', '5')
    g.add_edge('4', '3')
    g.add_edge('3', '5')
    g.add_edge('3', '4')
    g.add_edge('7', '1')
    g.add_edge('1', '7')
    g.add_edge('7', '4')
    g.add_edge('4', '7')
    g.add_edge('5', '0')
    g.add_edge('0', '5')


    print("***********")



if __name__ == "__main__":

    # testa_dijkstra()
    testa()


