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



    def dijkstra(self, chave, destino, visitado=list(), distancia=dict(), anterior=dict()):

        if chave not in self:
            raise TypeError('A raiz da arvore de caminho mais curto nao pode ser encontrado no grafo')
        if destino not in self:
            raise TypeError('O alvo do caminho mais curto nao pode ser encontrado no grafo')
            # finalizando a condição
        if chave == destino:
            # Contruir o caminho e mostramos ele
            caminho = []
            ant = destino
            while ant != None:
                caminho.append(ant)
                ant = anterior.get(ant, None)
            caminho.reverse()
            print('Menor caminho: ' + str(caminho) + " andou = " + str(distancia[destino]))
        else:
            if not visitado:
                distancia[chave] = 0  # procura nos vizinhos
            for vizinho in self[chave].neighbors:
                if vizinho not in visitado:
                    nova_distancia = distancia[chave] + int(self[chave].neighbors[vizinho])
                    if nova_distancia < distancia.get(vizinho, float('inf')):
                        distancia[vizinho] = nova_distancia
                        anterior[vizinho] = chave

            visitado.append(chave)

            unvisitado = {}
            for k in self:
                if k not in visitado:
                    unvisitado[k] = distancia.get(k, float('inf'))
            x = min(unvisitado, key=unvisitado.get)  # dos visitados, pega o c/ menor custo
            self.dijkstra(x, destino, visitado, distancia, anterior)

    def __str__(self):
        """ Shows the graph's adjacency list """

        str_g = ''

        for key in sorted(list(self.keys())):
            str_g += key + ' --> ' + str(self[key].neighbors) + '\n'

        return str_g

