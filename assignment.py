from helper_class.Graph import Graph

from BFS import BFS
from DFS import DFS
from TopologicalSort import topological_sort_matrix

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

# print('#' * 50)
# print('DFS')
# print('#' * 50)
#
# dfs = DFS(graph)
# dfs.search(3)

print('DFS Recursion')
print('#' * 50)

graph.show_graph()
dfs = DFS(graph)
dfs.search_w_recursion(3)

print('#' * 50)
print('Topological Sort')
print('#' * 50)

print('-------------------')
print('Case 1')
print('-------------------')

graph_T = Graph(graph.graph, 4)
print("Graph:", )
graph_T.show_graph()

order = topological_sort_matrix(graph.graph)

if order is None:
    print("Graph has a cycle!")
else:
    print("Topological order:", order)

print('-------------------')
print('Case 2')
print('-------------------')

graph = [
  [0, 1, 0, 0],
  [0, 0, 1, 0],
  [0, 0, 0, 1],
  [0, 0, 0, 0],
]

graph_T = Graph(graph, 4)
print("Graph:",)
graph_T.show_graph()

order = topological_sort_matrix(graph)

if order is None:
    print("Graph has a cycle!")
else:
    print("Topological order:", order)