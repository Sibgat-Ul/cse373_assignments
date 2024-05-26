from helper_class.Graph import Graph
from helper_class.Stack import Stack

class DFS:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.stack = Stack()
        self.size = graph.get_len()
        self.visited = [False] * self.size
        self.color = ['w'] * self.size

    def search(self, root: int) -> None:
        search_list = []

        self.graph.show_graph()
        level = 0

        time = 0
        d = [0] * self.size
        f = [0] * self.size

        previous = [-1] * self.size

        self.stack.push(root)

        while not self.stack.is_empty():
            root = self.stack.pop()
            neighbours = self.graph.get_neighbour(root)

            self.color[root] = 'g'
            self.visited[root] = True
            search_list.append(root)
            time += 1
            d[root] = time

            for n in neighbours:
                if self.color[n] == 'w':
                    self.stack.push(n)
                    self.color[n] = 'g'
                    self.visited[n] = True
                    previous[n] = root

            time += 1
            f[root] = time
            self.color[root] = 'b'

            print('-------------------')
            print('root: ', root)
            print('neighbours: ', neighbours)
            print('stack: ', self.stack.display())
            print('visited: ', self.visited)
            print('color: ', self.color)
            print('d: ', d)
            print('f: ', f)

        print('-------------------')
        print('search_list: ', search_list)