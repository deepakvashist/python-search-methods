from collections import deque

from search_methods.base import SearchAbstract


class Search(SearchAbstract):

    NAME = "Busca em Largura"

    def __init__(self, image_array):
        """
        Partindo de um vértice inicial, ela explora todos os vértices vizinhos.
        Em seguida, para cada vértice vizinho, ela repete esse processo,
        visitando os vértices ainda inexplorados.
        A Busca em Largura utiliza filas.
        """
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
