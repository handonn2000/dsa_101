from collections import defaultdict
from collections import deque

class AdjacencyList:
    def __init__(self) -> None:
        self.graph = defaultdict(set)

    def display(self):
        for vertex, edges in self.graph.items():
            print(vertex, '->', edges)

    def add_edge(self, v1, v2):
        self.graph[v1].add(v2)

    def dfs(self):
        visited = set()
        ans = []
        def traverse(v):
            if v in visited:
                return

            ans.append(v)        
            visited.add(v)
            
            for edge in self.graph[v]:
                traverse(edge)
                
        traverse(0)
        return ans

    def bfs(self):
        ans = []
        visited = set({0})
        queue = deque({0})
        while queue:
            v = queue.popleft()

            visited.add(v)
            ans.append(v)
            
            for neighbour in self.graph[v]:
                if neighbour not in visited:
                    queue.append(neighbour)
        
        return ans




# graph = {'0': set(['1', '2']),
#          '1': set(['0', '3', '4']),
#          '2': set(['0']),
#          '3': set(['1']),
#          '4': set(['2', '3'])}
graph = AdjacencyList()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 0)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 0)
graph.add_edge(3, 1)
graph.add_edge(4, 2)
graph.add_edge(4, 3)
graph.display()
print("DFS: " + str(graph.dfs()))
print("BFS: " + str(graph.bfs()))

