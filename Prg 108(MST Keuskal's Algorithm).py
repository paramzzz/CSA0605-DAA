class UnionFind:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2
                if self.rank[root1] == self.rank[root2]:
                    self.rank[root2] += 1

def kruskal_mst(graph):
    
    graph.sort()

    vertices = set()
    for _, vertex1, vertex2 in graph:
        vertices.add(vertex1)
        vertices.add(vertex2)
    uf = UnionFind(vertices)

    mst = []

    for cost, vertex1, vertex2 in graph:
        if uf.find(vertex1) != uf.find(vertex2):
            uf.union(vertex1, vertex2)
            mst.append((vertex1, vertex2, cost))

    return mst

graph = [
    (2, 'A', 'B'),
    (3, 'A', 'C'),
    (1, 'B', 'C'),
    (4, 'B', 'D'),
    (5, 'C', 'D')
]

mst = kruskal_mst(graph)

print("Minimum Cost Spanning Tree:")
for edge in mst:
    print(f"{edge[0]} --{edge[2]}--> {edge[1]}")
