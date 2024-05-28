from helper_class.Queue import Queue
from helper_class.Graph import Graph


class BFS:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.queue = Queue()
        self.size = graph.get_len()

        self.visited = [0] * self.size
        self.color = ['w'] * self.size
        self.d = [0] * self.size

    def search(self, root: int) -> None:
        search_list = []

        self.graph.show_graph()
        self.d[root] = 0

        self.color[root] = 'g'
        self.visited[root] = True
        self.queue.enqueue(root)

        while not self.queue.is_empty():
            root = self.queue.dequeue()
            neighbours = self.graph.get_neighbour(root)

            self.color[root] = 'g'
            self.visited[root] = True
            search_list.append(root)

            for n in neighbours:
                if not self.visited[n]:
                    self.d[n] = self.d[root] + 1
                    self.queue.enqueue(n)
                    self.color[n] = 'g'
                    self.visited[n] = True

            self.color[root] = 'b'

            print('-------------------')
            print('root: ', root)
            print('neighbours: ', neighbours)
            print('queue: ', self.queue.display())
            print('color: ', self.color)

        print('-------------------')
        print('search_list: ', search_list)