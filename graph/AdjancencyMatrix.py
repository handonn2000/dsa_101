class AdjMatrixGraph:
    def __init__(self, size) -> None:
        self.size = size
        self.adj_matrix = []
        for row in range(size):
            self.adj_matrix.append([0]* self.size)

    def display(self):
        for row in range(self.size):
            data = str(self.adj_matrix[row])
            print(data)

    def add_edge(self, v1, v2):
        if v1 != v2:
            self.adj_matrix[v1][v2] = 1
            self.adj_matrix[v2][v1] = 1

    def dfs(self):
        ans = []
        visited = set()
        return ans


    def bfs(self):
        pass
    
graph = AdjMatrixGraph(5)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.display()
print()
print("DFS: " + str(graph.dfs()))
print("BFS: " + str(graph.bfs()))