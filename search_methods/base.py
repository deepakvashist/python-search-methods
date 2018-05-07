import os
import copy
import time

from PIL import Image


class SearchAbstract:

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    SOLUTION_COLOR = [134, 1, 255, 255]

    def __init__(self, image_array):
        self.image_array = image_array
        self.image_solution_array = copy.deepcopy(self.image_array)
        self.graph = {}
        self.solution = None
        self.analyzed_states = 0
        self.start_time = time.time()

    def graph_solution(self):
        return NotImplementedError

    def get_problem_image_solution(self):
        image = Image.fromarray(self.image_solution_array)
        image.save(os.path.join(self.BASE_DIR, 'response', 'image.png'))

    def get_search_response_payload(self):
        print('Método usado: {}'.format(self.NAME))
        print('Tempo de resolução: {} ms'.format(time.time() - self.start_time))
        print('Número de estados analisados: {}'.format(self.analyzed_states))

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

    def build_maze_solution(self):
        position = list(self.graph.keys())[0]
        for step in self.solution:
            if step == 'L':
                position = (position[0], position[1] - 1)
            elif step == 'T':
                position = (position[0] - 1, position[1])
            elif step == 'B':
                position = (position[0] + 1, position[1])
            else:
                position = (position[0], position[1] + 1)

            self.image_solution_array[position[0]][position[1]] = \
                self.SOLUTION_COLOR
