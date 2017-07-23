"""
This module contains the classes Graph and Vertex, and implements functions related to graphs according to graph theory.
The Graph class implemented in this module represents a structured graph in the form of an adjacency list.

The advantages and disadvantages of using an adjacency list are:

Pros: Quick and uses less space for sparse graphs.
Cons: It's slow for dense graphs. """

import math

from collections import defaultdict
from time import sleep


class Vertex:
    """
    This class implements a vertex. In graph theory, a vertex (plural vertices) or node is the fundamental unit
    from which the graphs are formed. """

    def __init__(self, name):
        """
        Receives the name of the vertex and creates a list of neighbors.

        :param name: The vertex' name
        """

        self.name = str(name)
        self.neighbors = defaultdict(list)

    def __str__(self):
        """
        Representation of the vertex in the form of a string as its name.

        :return: The vertex' name
        """

        return self.name

    def __repr__(self):
        """
        Detailed representation of the Vertex object in the form of a string.

        :return: The vertex' name
        """

        return 'Vertex(%r, %r)' % (self.name, self.neighbors)

    def add_neighbor(self, v, weight=math.inf):
        """
        Adds a new neighbor (adjacent vertex) to the neighbors list.

        :param v: The new neighbor
        :param weight: The weight of the edge connecting the neighbor to the vertex in question,
                       if not informed, assumes the infinite value.
        """

        # if v not in self.neighbors:
        #     self.neighbors[v] = weight

        self.neighbors[v].append(weight)

    @property
    def degree(self):
        """
        Returns the degree of the vertex.

        :return: The vertex' degree
        """

        return len(self.neighbors)


class Graph(dict):
    """
    This class implements a graph structure. A graph is composed by sets of vertices connected by edges.

    In mathematics, and more specifically in graph theory, a graph is a structure amounting to a set of objects in
    which some pairs of the objects are in some sense "related". The objects correspond to mathematical abstractions
    called vertices (also called nodes or points) and each of the related pairs of vertices is called an edge
    (also called an arc or line).
    """

    def __init__(self, name='Graph', is_directed=False):

        super(Graph, self).__init__()

        self.name = name
        self.is_directed = is_directed

    def __str__(self):
        """
        Represents the graph in the form of an adjacency list.

        :return: A string representing the graph's adjacency list.
        """

        str_g = ''

        for key in sorted(list(self.keys())):
            str_g += key + ' --> ' + str(self[key].neighbors) + '\n'

        return str_g

    def add_vertex(self, vertex):
        """
        Adds a new vertex to the graph.

        :param vertex: The vertex to be added. It can be a string, an integer, or an instance of Vertex.
        :return: True if it have succeeded in adding the new vertex or False otherwise.
        """

        if isinstance(vertex, Vertex) and vertex.name not in self:
            self[vertex.name] = vertex
            return True
        if isinstance(vertex, str) and vertex not in self:
            self[vertex] = Vertex(vertex)
            return True
        if isinstance(vertex, int):
            vertex = str(vertex)
            if vertex not in self:
                self[vertex] = Vertex(vertex)
                return True
        return False

    def rm_vertex(self, vertex):
        """
        Removes the received vertex if it exists.

        :param vertex: The vertex to be removed
        """

        if not isinstance(vertex, str):
            vertex = str(vertex)

        if vertex in self:
            for v in self[vertex].neighbors:
                for u in self[v].neighbors:
                    if u == vertex:
                        self[v].neighbors.pop(vertex)
                        break
            self.pop(vertex)

    def add_edge(self, u, v, weight=math.inf):
        """
        Adds an edge between two vertices of the graph.
        Optionally adds a weight to the edge.

        :param u: The first vertex
        :param v: The second vertex
        :param weight: The weight of the edge, if not defined, assumes the infinite value.
        :return: True if it have succeeded in adding the edge or False otherwise.
        """

        if u in self and v in self:
            for key, value in self.items():
                if key == u:
                    value.add_neighbor(v, weight)
                if self.is_directed:
                    break
                if key == v:
                    value.add_neighbor(u, weight)
            return True
        else:
            return False

    def rm_edge(self, v, u):
        """
        Removes the edge between the received vertices if it exists.

        :param v: The first vertex
        :param u: The second vertex
        """

        if u in self and v in self:
            if u in self[v].neighbors:
                self[v].neighbors.pop(u)
            if v in self[u].neighbors:
                self[u].neighbors.pop(v)

    def is_connected(self, found=set(), start=None):
        """
        Checks if the graph is connected.

        :param found: A set of vertices found.
        :param start: The initial vertex.
        :return: True if it's a connected graph or False otherwise
        """

        vertices = list(self.keys())
        vertices.sort()

        if not start:
            start = vertices[0]

        found.add(start)

        if len(found) != len(vertices):
            for v in self[start].neighbors:
                if v not in found:
                    if self.is_connected(found, v):
                        return True
        else:
            return True

        return False

    @property
    def min_degree(self):
        """
        Find the lowest degree of vertex in the graph.

        :return: The lowest degree
        """

        min_degree = math.inf

        for vertex in self:
            degree = self[vertex].degree

            if degree < min_degree:
                min_degree = degree

        return min_degree

    @property
    def max_degree(self):
        """
        Find the greatest degree of vertex in the graph.

        :return: The greatest degree
        """

        max_degree = 0

        for vertex in self:
            degree = self[vertex].degree

            if degree > max_degree:
                max_degree = degree
        return max_degree

    @property
    def density(self):
        """
        Calculates the density of the graph using the formula:
        2 * edges / (vertices * (vertices - 1))

        :return: The graph density value
        """

        v = len(self.keys())
        e = len(list(self.edges))

        return 2.0 * e / (v * (v - 1))

    @property
    def diameter(self):
        """
        Calculate the diameter of a graph by finding the largest possible path
        between the two vertices in the graph.

        :return: The diameter of the graph
        """

        v = list(self.vertices)

        pairs = [(v[i], v[j]) for i in range(len(v) - 1) for j in range(i + 1, len(v))]

        print(pairs)

        smallest_paths = list()

        for (s, e) in pairs:
            paths = self.bfs_paths(s, e)
            if e == 'E':
                print('>>>', (s, e), len(list(paths)))
            sleep(2)
            smallest = sorted(paths, key=lambda x: len(x))[0]
            smallest_paths.append(smallest)

        smallest_paths.sort(key=len)

        diameter = len(smallest_paths[-1])

        return diameter

    @staticmethod
    def is_degree_sequence(sequence):
        """
        Given an undirected graph, a degree sequence is a monotonic non-increasing
        sequence of the vertex degrees (valencies) of its graph vertices.
        This method returns True if the graph has a degree sequence

        :param sequence: A graph's degree vertex sequence.
        :return: True if the graph has a degree sequence
        """
        return all(x >= y for x, y in zip(sequence, sequence[1:]))

    @staticmethod
    def erdoes_gallai(d_sequence):
        """
        The Erdös-Gallai Theorem states that the sequence (di) i = 1, ..., n being di >= di + 1
        is a degree sequence of a simple graph if the sum of the sequence is even and
        (d[i])i=1, ..., n <= k(k - 1) + min(d[i], k)i=k+1, .., n   for  k in {1, ..., n}

        :param d_sequence: The degree sequence of a graph
        :return: True if the Erdös-Gallai is fulfilled or False otherwise
        """

        if sum(d_sequence) % 2:
            # sum of sequence is odd
            return False

        if Graph.is_degree_sequence(d_sequence):
            for k in range(1, len(d_sequence) + 1):
                left = sum(d_sequence[:k])
                right = k * (k - 1) + sum([min(x, k) for x in d_sequence[k:]])
                if left > right:
                    return False
        else:
            # sequence is increasing
            return False
        return True

    @property
    def degree_sequence(self):
        """
        Returns the vertices' degree sequence of the graph.

        :return: Returns an inversely sorted tuple containing all the vertices degrees.
        """

        seq = list()

        for vertex in self:
            seq.append(self[vertex].degree)

        seq.sort(reverse=True)

        return tuple(seq)

    @property
    def isolated_vertices(self):
        """
        Finds all the isolated vertices.

        :return: The isolated vertices list or an empty list if there isn't any isolated vertex.
        """

        isolated = list()

        for v in self:
            if not self[v].neighbors:
                isolated.append(v)

        return isolated

    @property
    def vertices(self):
        """
        Returns all the vertex in the graph.

        :return: An iterator over graph's vertices list.
        """

        return iter(self.keys())

    @property
    def edges(self):
        """
        Returns all the edges in the graph.

        :return: A generator that iterates over all the edges in the graph
        """

        # visited = list()

        for v in self:
            for neighbor in self[v].neighbors:
                # if {v, neighbor} not in visited:
                    # visited.append(set((v, neighbor)))    # Ignore duplicates
                    # yield(v, neighbor)
                yield (v, neighbor)

    # Breadth-First Search Methods ==============================================

    def i_bfs(self, start, target):
        """
        Search for a given target vertex using the iterative Breadth-First Search algorithm.

        :param start: The initial vertex
        :param target: The target vertex to be find
        :return: True if the target vertex is found or False otherwise
        """

        queue, visited = [start], list()

        while queue:
            current = queue.pop(0)
            if current == target:
                return visited + [current]

            if current not in visited:
                queue.extend(set(self[current].neighbors) - set(visited))
                visited += [current]
        return None

    def r_bfs(self, start, target, visited=None):
        """
        Search for target vertex demonstrating how to make a recursive Breadth-First Search

        :param start: The initial vertex
        :param target: The target vertex to be find
        :param visited: A list to control which vertices have been visited and do not need to be visited again.
        :return: A list containing all vertices that have been visited until the target is found or None otherwise.
        """

        if not visited:
            visited = list()

        if isinstance(start, list):
            visited.extend([v for v in start if v not in visited])
        else:
            visited.append(start)

        if target in visited:
            return visited

        if len(visited) >= len(self.keys()):
            return None

        same_level_nodes = list()

        for v in start:
            #  Does not consider neighbors that are vertices already visited.
            neighbors = [u for u in self[v].neighbors if u not in visited]
            # List of vertices of the same level, without considering repeated vertices.
            same_level_nodes.extend([u for u in neighbors if u not in same_level_nodes])

        return self.r_bfs(same_level_nodes, target, visited)

    def bfs_paths(self, start, target):
        """
        Returns a generator for all possible paths between a vertex S and a vertex T.
        Uses the Breadth-First Search method with backtracking.

        :param start: The initial vertex
        :param target: The target vertex to be find
        """

        queue = [(start, [start])]

        while queue:
            current, path = queue.pop(0)
            if current == target:
                yield path
            for vertex in set(self[current].neighbors) - set(path):
                queue.extend([(vertex, path + [vertex])])

    # Depth-First Search Methods ==============================================

    def i_dfs(self, start, target):
        """
        Search for a given target vertex using the iterative Depth-First Search algorithm.

        :param start: The initial vertex
        :param target: The target vertex to be find
        :return: True if the target vertex is found or False otherwise
        """
        stack, visited = [start], list()

        while stack:
            current = stack.pop()

            if current == target:
                return visited + [current]

            if current not in visited:
                visited.append(current)
                stack.extend(set(self[current].neighbors) - set(visited))

        return None

    def r_dfs(self, start, target, visited=None):
        """
        Search for a given target vertex using the recursive Depth-First Search algorithm.

        :param start: The initial vertex
        :param target: The target vertex to be find
        :param visited: A list to control which vertices have been visited and do not need to be visited again.
        :return: A list containing all vertices that have been visited until the target is found or None otherwise.
        """

        if not visited:
            visited = list()

        visited.append(start)

        for v in set(self[start].neighbors) - set(visited):

            if target not in visited:
                self.r_dfs(v, target, visited)

            if target in visited:
                return visited

        # return None

    def dfs_paths(self, start, target, visited=None):
        """
        Returns a generator for all possible paths between a vertex S and a vertex T.
        Uses the Depth-First Search method with backtracking.

        :param start: The initial vertex
        :param target: The target vertex to be find
        :param visited: A list to control which vertices have been visited and do not need to be visited again.
        """

        if not visited:
            visited = [start]

        if start == target:
            yield visited

        for vertex in [x for x in self[start].neighbors if x not in visited]:
            for each_path in self.dfs_paths(vertex, target, visited + [vertex]):
                yield each_path  # return the paths generator

    # ----------------------------------------------------------

    def dijkstra(self, start, target, visited=None, distances=None, previous=None):

        if not visited:
            visited = list()
        if not distances:
            distances = dict()
        if not previous:
            previous = dict()

        if start not in self:
            raise TypeError('Start vertex cannot be found in the graph.')
        if target not in self:
            raise TypeError('The target vertex does not exist in the graph.')

        if start == target:
            path = list()
            ant = target

            while ant:
                path.append(ant)
                ant = previous.get(ant, None)
            path.reverse()

            print('Smaller path: {}\nWeight: {}'.format(path, distances[target]))

        else:
            if not visited:
                distances[start] = 0
            for neighbor in self[start].neighbors:
                if neighbor not in visited:
                    new_distance = distances[start] + float(min(self[start].neighbors[neighbor]))
                    if new_distance < distances.get(neighbor, math.inf):
                        distances[neighbor] = new_distance
                        previous[neighbor] = start

            visited.append(start)

            unvisited = {}

            for k in self:
                if k not in visited:
                    unvisited[k] = distances.get(k, math.inf)
            x = min(unvisited, key=unvisited.get)

            self.dijkstra(x, target, visited, distances, previous)


    ''' TODO Implementar:
    
        arestas paralelas
        achar arestas incidentes a um grafp
        mostar vertices adjacentes a um vertice
        mostrar os adjacentes entre sí
        mostrar arestas adjacentes
        mostrar laços
        verificar se é simples, sem arestas paralelas e laços
        Grafo direcionado
        mostrar se é grafo completo
        qtd de grafos distintos
        se é grafo ciclo
        é um ciclo  OBS grafo ciclo é aquele que é um circulo e não um ciclico que é aquele que possui um ou mais ciclos
        é aciclico
        is wheel vertex
        se é grafo roda
        se é grafo cubo
        se é bipartido
        se é bipartido completo
        é grafo estrela?
        complemento de um grafo
        multigrafo
        pseudografo
        multigrafo dirigido
        hipergrafo
        valorado
        is regular graph?
        
        imersível
        subgrafo
        grafo regular
        matriz adjacencia dirigido e não dirigido
        matriz incidencia
        ver se são isomorfos
        árvores e arvores geradoras
        florestas \||||||
        homromorfos
        caminho euleriano e hamiltoniano
        V. J. Havel (1955) e S. L. Hakimi
(1961) e S. A. Choudum.

        '''
