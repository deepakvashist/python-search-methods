from collections import deque

from search_methods.base import SearchAbstract


class Search(SearchAbstract):
    """
    Um algoritmo de busca é um algoritmo que percorre um grafo andando
    pelos arcos de um vértice a outro. Um algoritmo de busca examina
    sistematicamente os vértices e os arcos do grafo depois de examinar a
    ponta inicial de um arco, o algoritmo percorre o arco e examina sua
    ponta final. Cada arco é examinado no máximo uma vez.
    (https://www.ime.usp.br/~pf/algoritmos_para_grafos/aulas/bfs.html)
    """

    NAME = "Busca em Largura"

    def __init__(self, image_array):
        super(Search, self).__init__(image_array)
        print(self.search())

    def get_problem_image_solution(self):
        pass

    def get_search_response_payload(self):
        pass

    def search(self):
        start, goal = (0, 152), (321, 168)
        queue = deque([('', start)])
        visited = set()

        while queue:
            path, current = queue.popleft()
            if current == goal:
                return path
            if current in visited:
                continue

            visited.add(current)

            for direction, neighbour in self.graph[current]:
                queue.append((path + direction, neighbour))
