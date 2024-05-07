from collections import deque

class AdjMatrixGraph:
    def __init__(self, size) -> None:
        self.size = size
        self.graph = []
        for _ in range(size):
            self.graph.append([0] * self.size)

    def display(self):
        for row in range(self.size):
            data = str(self.graph[row])
            print(data)

    def add_edge(self, v1, v2):
        if v1 != v2:
            self.graph[v1][v2] = 1
            self.graph[v2][v1] = 1
    
    def dfs(self):
        visited = [False] * self.size
        traversal_order = []

        # Recursive traverse
        def traverse(i):
            visited[i] = True
            traversal_order.append(i)

            for j in range(self.size):
                if self.graph[i][j] == 1 and not visited[j]:
                    traverse(j)

        # Visit all vertex that are not visited yet (in case where there are more than 1 connected component)
        for vertex, is_visited in enumerate(visited):
            if not is_visited:
                traverse(vertex)
        return traversal_order

    def bfs(self):
        ans = []
        visited = [False] * self.size
        def traverse(start):
            queue = deque({start})
            while queue:
                i = queue.popleft()

                visited[i] = True
                ans.append(i)
                for j in range(self.size):
                    if not visited[j] and self.graph[i][j] == 1:
                        visited[j] = True
                        queue.append(j)

        for vertex, is_visited in enumerate(visited):
            if not is_visited:
                traverse(vertex)
        return ans
    
    def connected_component(self):
        count = 0
        visited = set()

        def dfs(v):
            visited.add(v)

            for u in range(self.size):
                if self.graph[v][u] == 1 and u not in visited:
                    dfs(u)

        for v in range(self.size):
            if v not in visited:
                count += 1
                dfs(v)
        return count

            
graph = AdjMatrixGraph(5)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
# graph.add_edge(2, 3)
graph.add_edge(3, 4)
graph.display()
print()
print("DFS: " + str(graph.dfs()))
print("BFS: " + str(graph.bfs()))
print("Connected Component: " + str(graph.connected_component())) # 1

