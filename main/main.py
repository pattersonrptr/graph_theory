from graph.graph_adjl import Graph
from graph.graph_adjl import Vertex

if __name__ == "__main__":
    graph = Graph()

    # for i in range(ord('A'), ord('G')):
    for i in range(0, 8):

        # graph.add_vertex(Vertex(chr(i)))
        graph.add_vertex(Vertex(str(i)))

    # edges = ['AB5', 'AE1', 'BF3', 'CG4', 'DE5', 'DH6', 'EH7', 'FG2', 'FI5', 'FJ9', 'GJ2', 'HI5']
    # edges = ['AB4', 'AC3', 'BD2', 'CB1', 'CD2', 'CE2', 'DF2', 'EF3']

    # (0) ←──────→ (2) <──────> (6)
    #  ↑   ↖                     ↑
    #  │     \                   │
    #  │      \                  │
    #  │       ↘(7)              │
    #  │         ↑               │
    #  │         │               │
    #  │         └─→ (1)         │
    #  │                         │
    #  ↓                         ↓
    # (5) ←──────→ (3) <──────> (4)
    #  ↑                         ↑
    #  │                         │
    #  └─────────────────────────┘

    edges = ['02', '05', '07', '26', '20', '53', '50', '54', '71', '70', '74', '17', '47', '46', '45', '43', '34', '35']

    for edge in edges:
        # graph.add_edge(edge[1:2], edge[:-2], edge[2:])
        graph.add_edge(edge[1:], edge[:1])

    print(graph)

    # print(graph.i_dfs('0', '1'))
    print(graph.r_dfs('0', '1'))

    for p in graph.dfs_paths('0', '1'):
        print(p)

    graph.dijkstra('0', '1')

