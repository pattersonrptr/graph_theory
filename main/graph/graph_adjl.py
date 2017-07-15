"""
Adjacency lists
pro: rápida e usa menos espaço para grafos esparsos
con: lenta para grafos densos
"""

class Vertex:
    def __init__(self, name):
        self.name = str(name)
        self.neighbors = dict()

    def add_neighbor(self, v, weight=0):
        if v not in self.neighbors:
            self.neighbors[v] = weight


class Graph(dict):

    def add_vertex(self, vertex):

        if isinstance(vertex, Vertex) and vertex.name not in self:
            self[vertex.name] = vertex
            return True
        else:
            return False

    def rm_vertex(self, vertex):
        if vertex in self:
            for v in self[vertex].neighbors:
                for u in self[v].neighbors:
                    if u == vertex:
                        self[v].neighbors.pop(vertex)
                        break
            self.pop(vertex)

    def add_edge(self, u, v, weight=0):

        if u in self and v in self:
            for key, value in self.items():
                if key == u:
                    value.add_neighbor(v, weight)
                if key == v:
                    value.add_neighbor(u, weight)
            return True
        else:
            return False

    def rm_edge(self, v, u):

        if u in self and v in self:
            if u in self[v].neighbors:
                self[v].neighbors.pop(u)
            if v in self[u].neighbors:
                self[u].neighbors.pop(v)

    def is_connected(self, found=set(), start=None):

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

    def get_degree(self, vertex):
        return len(self[vertex].neighbors)

    @property
    def min_degree(self):

        min_degree = 100000000

        for vertex in self:
            degree = self.get_degree(vertex)

            if degree < min_degree:
                min_degree = degree
        return min_degree

    @property
    def max_degree(self):

        max_degree = 0

        for vertex in self:
            degree = self.get_degree(vertex)

            if degree > max_degree:
                max_degree = degree
        return max_degree

    @property
    def density(self):

        v = len(self.keys())
        e = len(self.edges)

        return 2.0 * e / (v * (v - 1))

    @property
    def diameter(self):
        # TODO: verificar se esta função esta funcionando do jeito certo!

        v = self.vertices

        pairs = [(v[i], v[j]) for i in range(len(v) - 1) for j in range(i + 1, len(v))]

        smallest_paths = list()

        for (s, e) in pairs:
            # paths = self.find_all_paths(s, e)
            paths = self.bfs_paths(s, e)
            smallest = sorted(paths, key=len)[0]
            smallest_paths.append(smallest)

        smallest_paths.sort(key=len)

        diameter = len(smallest_paths[-1])

        return diameter

    @staticmethod
    def is_degree_sequence(sequence):
        return all(x >= y for x, y in zip(sequence, sequence[1:]))

    @staticmethod
    def erdoes_gallai(dsequence):

        if sum(dsequence) % 2:
            # sum of sequence is odd
            return False

        if Graph.is_degree_sequence(dsequence):
            for k in range(1, len(dsequence) + 1):
                left = sum(dsequence[:k])
                right = k * (k - 1) + sum([min(x, k) for x in dsequence[k:]])
                if left > right:
                    return False
        else:
            # sequence is increasing
            return False
        return True

    # def adjacency_matrix(self):
    #
    #     keys = sorted(self.keys())
    #     size = len(keys)
    #
    #     matrix = [[0] * size for _ in range(size)]
    #
    #     for a, b in [(keys.index(a), keys.index(b)) for a, row in self.items() for b in row]:
    #         matrix[a][b] = 2 if (a == b) else 1
    #
    #     return matrix

    @property
    def degree_sequence(self):

        # seq = dict()
        #
        # for vertex in self:
        #     seq[vertex] = self.get_degree(vertex)
        #
        # seq = sorted(seq.items(), key=lambda x: x[1])
        #
        # return seq

        seq = []

        for vertex in self:
            seq.append(self.get_degree(vertex))

        seq.sort(reverse=True)

        return tuple(seq)

    @property
    def isolated_vertices(self):

        isolated = list()

        for v in self:
            if not self[v].neighbors:
                isolated.append(v)
        return isolated

    @property
    def vertices(self):
        return list(self.keys())

    @property
    def edges(self):
        edges = list()

        for v in self:
            for neighbor in self[v].neighbors:
                if {neighbor, v} not in edges:
                    edges.append({v, neighbor})
        return edges

    # Breadth-First Search Methods ==============================================

    def i_bfs(self, start, target):

        queue, visited = [start], list()

        while queue:
            current = queue.pop(0)
            if current == target:
                return visited + [current]

            if current not in visited:
                queue.extend(set(self[current].neighbors) - set(visited))
                visited += [current]
        return False

    def r_bfs(self, start, target, visited=list()):

        visited.extend(start)

        if target in visited:
            return visited

        same_level_nodes = list()

        for v in start:
            #  Does not consider neighbors that are vertices already visited.
            neighbors = [u for u in self[v].neighbors if u not in visited]
            # List of vertices of the same level, without considering repeated vertices.
            same_level_nodes.extend([u for u in neighbors if u not in same_level_nodes])

        return self.r_bfs(same_level_nodes, target, visited)

    def bfs_paths(self, start, target):

        queue = [(start, [start])]

        while queue:
            current, path = queue.pop(0)
            if current == target:
                yield path
            for vertex in set(self[current].neighbors) - set(path):
                queue.extend([(vertex, path + [vertex])])

    # Depth-First Search Methods ==============================================

    def i_dfs(self, start, target):

        stack, visited = [start], list()

        while stack:
            current = stack.pop()

            if current == target:
                return True

            if current not in visited:
                visited.append(current)
                stack.extend(set(self[current].neighbors) - set(visited))

        return False

    def r_dfs(self, start, target, visited=set()):

        visited.add(start)

        for v in set(self[start].neighbors) - visited:

            self.r_dfs(v, target, visited)

            if target in visited:
                return True

        return False

    def dfs_paths(self, start, target, path=list()):

        if not path:
            path = [start]

        if start == target:
            yield path

        for vertex in [x for x in self[start].neighbors if x not in path]:
            for each_path in self.dfs_paths(vertex, target, path + [vertex]):
                yield each_path  # return the paths generator

    # ----------------------------------------------------------

    def dijkstra(self, start, target, visited=list(), distances=dict(), previous=dict()):

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
                    new_distance = distances[start] + int(self[start].neighbors[neighbor])
                    if new_distance < distances.get(neighbor, float('inf')):
                        distances[neighbor] = new_distance
                        previous[neighbor] = start

            visited.append(start)

            unvisited = {}

            for k in self:
                if k not in visited:
                    unvisited[k] = distances.get(k, float('inf'))
            x = min(unvisited, key=unvisited.get)

            self.dijkstra(x, target, visited, distances, previous)

    def __str__(self):
        """ Shows the graph's adjacency list """

        str_g = ''

        for key in sorted(list(self.keys())):
            str_g += key + ' --> ' + str(self[key].neighbors) + '\n'

        return str_g

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
        se é grafo roda
        se é grafo cubo
        se é bipartido
        se é bipartido completo
        multigrafo
        pseudografo
        multigrafo dirigido
        hipergrafo
        valorado
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
        '''
