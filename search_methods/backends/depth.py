from collections import deque

from search_methods.base import SearchAbstract


class Search(SearchAbstract):
    """
    O algoritmo de busca em profundidade visita todos os vértices e todos
    os arcos de um grafo dado e atribui um número a cada vértice: o k-ésimo
    vértice descoberto recebe o número k.
    (https://www.ime.usp.br/~pf/algoritmos_para_grafos/aulas/dfs.html)
    """

    NAME = "Busca em Profundidade"

    def __init__(self, image_array):
        super(Search, self).__init__(image_array)

    def graph_solution(self):
        start, goal = (0, 152), (321, 168)
        stack = deque([('', start)])
        visited = set()

        while stack:
            path, current = stack.pop()
            if current == goal:
                return path
            if current in visited:
                continue
            visited.add(current)
            for direction, neighbour in self.graph[current]:
                stack.append((path + direction, neighbour))
