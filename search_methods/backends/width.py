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
        self.graph_solution = {}
        self.graph_analysis()

    def get_problem_image_solution(self):
        pass

    def get_search_response_payload(self):
        pass

    def graph_analysis(self):
        past_row_positions = None

        for row in self.graph:
            if not past_row_positions:
                self.graph_solution[row] = self.graph[row]
                past_row_positions = self.graph[row]
                continue

            self.graph_solution[row] = []
            for i in self.graph[row]:
                if i in past_row_positions:
                    self.graph_solution[row].append(i)

            past_row_positions = self.graph_solution[row]
