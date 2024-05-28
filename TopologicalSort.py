def topological_sort_matrix(graph):
    n = len(graph)
    indegree = [0] * n

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                indegree[j] += 1

    queue = []
    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)

    order = []

    while queue:
        u = queue.pop(0)
        order.append(u)

        for v in range(n):
            if graph[u][v] == 1:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)

    if len(order) != n:
        return None  # Cycle detected

    return order


