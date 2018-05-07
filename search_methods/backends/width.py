from collections import deque

from search_methods.base import SearchAbstract


class Search(SearchAbstract):
    """
    A busca em largura é um algoritmo utilizado para percorrer ou buscar itens
    dentro das estruturas de dados grafos ou árvores. Como característica temos
    que a busca sempre ocorre nos filhos ou nós mais próximos ao nó pelo qual a
    busca foi iniciada.
    (https://blog.pantuza.com/artigos/busca-em-largura)
    """

    NAME = "Busca em Largura"

    def __init__(self, image_array):
        super(Search, self).__init__(image_array)

    def graph_solution(self):
        start = list(self.graph.keys())[0]
        goal = list(self.graph.keys())[-1]
        queue = deque([('', start)])
        visited = set()

        while queue:
            self.analyzed_states += 1
            path, current = queue.popleft()
            if current == goal:
                return path
            if current in visited:
                continue

            visited.add(current)

            for direction, neighbour in self.graph[current]:
                queue.append((path + direction, neighbour))
