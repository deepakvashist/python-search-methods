from collections import deque

from search_methods.base import SearchAbstract


class Search(SearchAbstract):

    NAME = "Busca em Profundidade"

    def __init__(self, image_array):
        super(Search, self).__init__(image_array)

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
