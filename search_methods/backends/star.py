from heapq import heappop, heappush

from search_methods.base import SearchAbstract


class Search(SearchAbstract):

    NAME = 'A*'

    def __init__(self, image_array):
        super(Search, self).__init__(image_array)

    def heuristic(self, cell, goal):
        return abs(cell[0] - goal[0]) + abs(cell[1] - goal[1])

    def graph_solution(self):
        start, goal = (0, 152), (321, 168)
        pr_queue = []
        heappush(pr_queue, (0 + self.heuristic(start, goal), 0, '', start))
        visited = set()

        while pr_queue:
            _, cost, path, current = heappop(pr_queue)
            if current == goal:
                return path
            if current in visited:
                continue
            visited.add(current)
            for direction, neighbour in self.graph[current]:
                heappush(pr_queue, (cost + self.heuristic(neighbour, goal), cost + 1,
                                    path + direction, neighbour))
