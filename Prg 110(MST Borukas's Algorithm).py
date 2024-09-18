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

def boruvka_mst(graph):
    
    mst = []

    vertices = set(graph.keys())
    uf = UnionFind(vertices)

    num_components = len(vertices)

    while num_components > 1:
        min_edges = {}

        for node, neighbors in graph.items():
            for neighbor, cost in neighbors.items():
                root1 = uf.find(node)
                root2 = uf.find(neighbor)

                if root1 != root2:
                    if root1 not in min_edges or cost < min_edges[root1][0]:
                        min_edges[root1] = (cost, node, neighbor)
                    if root2 not in min_edges or cost < min_edges[root2][0]:
                        min_edges[root2] = (cost, node, neighbor)

        for cost, node, neighbor in min_edges.values():
            mst.append((node, neighbor, cost))
            uf.union(node, neighbor)
            num_components -= 1

    return mst

graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 4},
    'C': {'A': 3, 'B': 1, 'D': 5},
    'D': {'B': 4, 'C': 5}
}

mst = boruvka_mst(graph)
print("Minimum Cost Spanning Tree:")
for edge in mst:
    print(f"{edge[0]} --{edge[2]}--> {edge[1]}")
