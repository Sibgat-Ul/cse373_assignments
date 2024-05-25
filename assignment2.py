from helper_class.Queue import Queue
from helper_class.Stack import Stack
from helper_class.Graph import Graph

from helper_class.BFS import BFS
from helper_class.DFS import DFS


graph = [
    [0, 1, 0, 1],
    [1, 0, 1, 1],
    [0, 1, 1, 1],
    [1, 0, 1, 0]
]

print('#' * 50)
print('BFS')
print('#' * 50)

graph = Graph(graph, 4)
bfs = BFS(graph)
bfs.search(3)

print('#' * 50)
print('DFS')
print('#' * 50)

dfs = DFS(graph)
dfs.search(3)
