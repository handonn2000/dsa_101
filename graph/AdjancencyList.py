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

    # TC:
    # SC:
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

    # TC:
    # SC:
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

    def connected_component(self):
        count = 0
        visited = set()
        def dfs(v):
            if v in visited:
                return
            visited.add(v)
            for u in self.graph[v]:
                if u not in visited:
                    dfs(u)

        for v in self.graph.copy():
            if v not in visited:
                count += 1
                dfs(v)
        
        return count


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
print("DFS: " + str(graph.dfs())) # [0, 1, 3, 4, 2] 
print("BFS: " + str(graph.bfs())) # [0, 1, 2, 3, 4]
print("Connected Component: " + str(graph.connected_component())) # 1
graph.add_edge(5, 6)
graph.add_edge(5, 7)
print("Connected Component: " + str(graph.connected_component())) # 2
graph.add_edge(4, 5)
print("Connected Component: " + str(graph.connected_component())) # 1



