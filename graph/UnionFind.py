class UnionFind:
    def __init__(self, size) -> None:
        self.parent = list(range(size))
        self.height = [1] * size

    def find(self, u):
        while self.parent[u] != u:
            u = self.parent[u]

        return u

    def union(self, u, v):
        parent_u = self.find(u)
        parent_v = self.find(v)
        if parent_u != parent_v:
            height_u = self.height[parent_u]
            height_v = self.height[parent_v]
            if height_u < height_v:
                self.parent[parent_u] = parent_v
            else:
                self.parent[parent_v] = parent_u
                self.height[parent_u] += 1


    def connected(self, u, v):
        return self.find(u) == self.find(v)
    



uf = UnionFind(5)
uf.union(1, 2)
uf.union(2, 3)
print(uf.connected(1, 3))  # True
print(uf.connected(1, 4))  # False
uf.union(3, 4)
print(uf.connected(1, 4))  # True


def is_biparti(graph, n):
    uf = UnionFind(n)

    for u in range(n):
        for v in graph[u]:
            if uf.connected(u, v):
                return False
            uf.union(graph[u][0], v)

    return True

graph1 = [[1,2,3],[0,2],[0,1,3],[0,2]]
graph2 = [[1,3],[0,2],[1,3],[0,2]]
print(is_biparti(graph1, len(graph1))) # False
print(is_biparti(graph2, len(graph2))) # True


