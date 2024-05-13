from collections import deque

def init(size):
    adjList = []
    for _ in range(size + 1):
        adjList.append([])


    add_edge(adjList, 1, 2)
    add_edge(adjList, 1, 6)
    add_edge(adjList, 2, 3)
    add_edge(adjList, 2, 4)
    add_edge(adjList, 3, 5)
    add_edge(adjList, 4, 5)
    add_edge(adjList, 7, 6)
    
    return adjList

def add_edge(adjList, i, j):
    adjList[i].append(j)

# DFS
def topo_dfs(adjList):
    n = len(adjList)
    visited = [False] * n
    topo = []
    def dfs(v):
        visited[v] = True

        for nei in graph[v]:
            if not visited[nei]:
                dfs(nei)

        topo.append(v)

    for v in range(1, n):
        if not visited[v]:
            dfs(v)

    return topo[::-1]

def indegree(adjList):
    n = len(adjList)
    ind = dict()
    for i in range(1, n):
        ind[i] = 0

    for i in range(n):
        for v in adjList[i]:
            ind[v] += 1

    return ind


# BFS
def topo_kahn(adjList):
    ind = indegree(adjList)
    queue = deque()
    for v, i in ind.items():
        if i == 0:
            queue.append(v)

    topo = []
    while queue:
        v = queue.popleft()
        topo.append(v)

        for nei in adjList[v]:
            ind[nei] -= 1
            if ind[nei] == 0:
                queue.append(nei)

    return topo


if __name__ == "__main__":
    graph = init(7)
    print(graph)
    # topo = topo_dfs(graph)
    # print(topo)
    kahn = topo_kahn(graph)
    print(kahn)