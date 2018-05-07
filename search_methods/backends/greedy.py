from search_methods.base import SearchAbstract


class Search(SearchAbstract):

    NAME = 'Greedy'

    def __init__(self, image_array):
        super(Search, self).__init__(image_array)

    def graph_solution(self):
        pass
