class SearchAbstract:

    def __init__(self, image_array):
        self.image_array = image_array
        self.graph = {}
        self.set_graph()

    def get_problem_image_solution(self):
        return NotImplementedError

    def get_search_response_payload(self):
        return NotImplementedError

    def set_graph(self):
        maze_height = len(self.image_array)
        maze_width = len(self.image_array[0])

        graph = {}

        for maze_row in range(maze_width):
            for maze_col in range(maze_height):
                if 0 in self.image_array[maze_row][maze_col]:
                    graph.update({(maze_row, maze_col): []})

        for row, col in graph.keys():
            if row < maze_height - 1 and 0 in self.image_array[row + 1][col]:
                graph[(row, col)].append(('B', (row + 1, col)))
                graph[(row + 1, col)].append(('T', (row, col)))
            if col < maze_width - 1 and 0 in self.image_array[row][col + 1]:
                graph[(row, col)].append(('R', (row, col + 1)))
                graph[(row, col + 1)].append(('L', (row, col)))

        self.graph = graph
