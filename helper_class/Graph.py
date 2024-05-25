class Graph:
    def __init__(self, graph, nodes, size=None):
        self.graph = graph

        if graph is None:
            self.graph = [[0] * size] * size
            self.size = size
        else:
            self.size = len(graph[0])

    def get_neighbour(self, root):
        neighbour = self.graph[root]
        nodes = []

        for i, n in enumerate(neighbour):
            if n == 1:
                nodes.append(i)

        return nodes

    def get_graph(self):
        return self.graph

    def show_graph(self):
        print(f'id:{[i for i in range(self.size)]}')

        for i in range(self.size):
            print(f'{i}: {self.graph[i]}')

    def get_len(self):
        return self.size
