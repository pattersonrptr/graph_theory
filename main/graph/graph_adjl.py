"""
Adjacency lists
pro: rápida e usa menos espaço para grafos esparsos
con: lenta para grafos densos
"""


class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors = dict()

    def add_neighbor(self, v, weight=0):
        if v not in self.neighbors:
            self.neighbors[v] = weight


class Graph(dict):
    # self = dict()

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

    def bfs(self, start, target):

        queue, visited = [start], list()
        while queue:
            current = queue.pop(0)
            if current == target:
                return visited + [current]
            if current not in visited:
                queue.extend(set(self[current].neighbors) - set(visited))
                visited += [current]
        return False

    def bfs_all(self, start, target):

        queue = [(start, [start])]
        while queue:
            current, path = queue.pop(0)
            if current == target:
                yield path
            for vertex in set(self[current].neighbors) - set(path):
                queue.extend([(vertex, path + [vertex])])

    # Depth-First Search Methods ==============================================

    def i_dfs(self, start, target):
        """ Iterative Depth-First Search. """

        stack, visited = [start], list()
        while stack:
            current = stack.pop()

            if current == target:
                return True

            if current not in visited:
                visited.append(current)
                stack.extend(set(self[current].neighbors) - set(visited))
        return False

    def r_dfs(self, start, target, visited=list()):
        """ Recursive Depth-First Search. """

        if target in visited:       # Prevents the dfs from proceeding because it has already found the target.
            return True

        visited.append(start)

        for v in set(self[start].neighbors) - set(visited):
            if v not in visited:
                self.r_dfs(v, target, visited)

        return True if target in visited else False

    def dfs_paths(self, start, target, path=list()):
        if not path:
            path = [start]
        if start == target:
            yield path
        for v in set(self[start].neighbors) - set(path):
            yield from self.dfs_paths(v, target, path + [v])

        def dfs_vertices(self, inicio, alvo, visitados=None):
            ''' Retorna todos os nós que podem ser visitados a partir de um nó inicial '''
            if visitados is None:
                visitados = []

            # Este IF vai parar a recursão quando achar o nó alvo, sem ele o algoritmo visitaria tos os os nós
            if alvo in visitados:
                return visitados

            if inicio in visitados:
                return

            visitados.append(inicio)
            # Percorre os vizinhos do vértice inicial/raiz
            for cada in [x for x in self[inicio] if x not in visitados]:
                self.dfs_vertices(cada, alvo,
                                  visitados)  # Chama recursivamente passando vinzinho e a lista de visitados

            return visitados if alvo in visitados else False

            # ----------------------------------------------------------

    def dfs_caminhos(self, inicio, alvo, caminho=None):

        if caminho is None:
            caminho = [inicio]

        if inicio == alvo:
            yield caminho

        for vertice in [x for x in self[inicio] if x not in caminho]:
            for cada_caminho in self.dfs_caminhos(vertice, alvo, caminho + [vertice]):
                yield cada_caminho  # Gera uma lista de caminhos

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

        str_g = ''
        for key in sorted(list(self.keys())):
            str_g += key + ' --> ' + str(self[key].neighbors) + '\n'

        return str_g

