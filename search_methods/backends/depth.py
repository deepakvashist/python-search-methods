from collections import deque

from search_methods.base import SearchAbstract


class Search(SearchAbstract):
    """
    A busca em profundidade é um algoritmo utilizado para percorrer ou buscar
    itens dentro das estruturas de dados grafos ou árvores. Sua característica
    básica é percorrer todos os nós filhos ao nó raiz o mais profundo possível
    para somente depois retroceder.
    (https://blog.pantuza.com/artigos/busca-em-profundidade)
    """

    NAME = "Busca em Profundidade"

    def __init__(self, image_array):
        super(Search, self).__init__(image_array)

    def graph_solution(self):
        start = list(self.graph.keys())[0]
        goal = list(self.graph.keys())[-1]
        stack = deque([('', start)])
        visited = set()

        while stack:
            self.analyzed_states += 1
            path, current = stack.pop()
            if current == goal:
                return path
            if current in visited:
                continue
            visited.add(current)
            for direction, neighbour in self.graph[current]:
                stack.append((path + direction, neighbour))
