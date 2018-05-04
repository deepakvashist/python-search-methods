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
        for row_index, image_row in enumerate(self.image_array):
            self.graph['pixels_column_{}'.format(row_index)] = []
            past_parent_index = 0

            for pixel_index, pixel in enumerate(image_row):
                if not all(pixel == [255, 255, 255, 255]) and \
                        past_parent_index + 1 != pixel_index:
                    self.graph['pixels_column_{}'.format(row_index)]. \
                        append(pixel_index)
                    past_parent_index = pixel_index
