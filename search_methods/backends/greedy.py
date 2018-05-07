from heapq import heappop, heappush

from search_methods.base import SearchAbstract


class Search(SearchAbstract):

    NAME = 'Greedy'

    def __init__(self, image_array):
        super(Search, self).__init__(image_array)

    def heuristic(self, cell, goal):
        return abs(cell[0] - goal[0]) + abs(cell[1] - goal[1])

    def graph_solution(self):
        start = list(self.graph.keys())[0]
        goal = list(self.graph.keys())[-1]
        pr_queue = []
        heappush(pr_queue, (0 + self.heuristic(start, goal), 0, '', start))
        visited = set()

        while pr_queue:
            self.analyzed_states += 1
            _, cost, path, current = heappop(pr_queue)
            if current == goal:
                return path
            if current in visited:
                continue
            visited.add(current)
            for direction, neighbour in self.graph[current]:
                heappush(pr_queue, (self.heuristic(neighbour, goal), cost + 1,
                                    path + direction, neighbour))
