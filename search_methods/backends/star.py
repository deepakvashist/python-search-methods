from heapq import heappop, heappush

from search_methods.base import SearchAbstract


class Search(SearchAbstract):
    """
    É um algoritmo para Busca de Caminho. Ele busca o caminho em um grafo de um
    vértice inicial até um vértice final. Ele é a combinação de aproximações
    heurísticas como do algoritmo Breadth First Search (Busca em Largura) e da
    formalidade do Algoritmo de Dijkstra.

    --> À medida que A * percorre o gráfico, segue um caminho do menor custo
        total ou distância esperado, mantendo uma fila de prioridade
        classificada de segmentos de caminho alternativo ao longo do caminho
    --> Usa uma busca gulosa e encontra um caminho de menor custo
    --> Ele usa uma função de custo heurístico do nó para determinar a ordem em
        que a pesquisa visita nós no gráfico
    --> A complexidade de tempo depende da heurística
    """

    NAME = 'A*'

    def __init__(self, image_array):
        super(Search, self).__init__(image_array)

    def heuristic(self, cell, goal):
        """
        Manhattan distance
        --> A distância entre dois pontos é a soma das diferenças absolutas de
            suas coordenadas.
        --> |x1 - x2| + |y1 - y2|
        """
        return abs(cell[0] - goal[0]) + abs(cell[1] - goal[1])

    def graph_solution(self):
        """
        ---> Utilizamos o módulo "heapq" para filas de prioridade e adicionar a
             parte de custo de cada elemento
        """
        start = list(self.graph.keys())[0]
        goal = list(self.graph.keys())[-1]
        pr_queue = []
        heappush(pr_queue, (0 + self.heuristic(start, goal), 0, '', start))
        visited = set()

        while pr_queue:
            self.analyzed_states += 1

            # Retona o menor item da lista
            # cost: Distância
            # path: Caminho percorrido
            # current: Nó atual
            _, cost, path, current = heappop(pr_queue)

            if current == goal:
                return path
            if current in visited:
                continue

            visited.add(current)

            for direction, neighbour in self.graph[current]:
                heappush(pr_queue, (cost + self.heuristic(neighbour, goal), cost + 1,
                                    path + direction, neighbour))
