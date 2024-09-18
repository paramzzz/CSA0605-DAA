class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

def kruskal_mst(edges, n):
    edges.sort(key=lambda x: x[2])
    mst_edges = []
    total_weight = 0
    disjoint_set = DisjointSet(n)
    for edge in edges:
        u, v, weight = edge
        if disjoint_set.find(u) != disjoint_set.find(v):
            mst_edges.append(edge)
            total_weight += weight
            disjoint_set.union(u, v)
    return mst_edges, total_weight

def is_unique_mst(edges, n, given_mst):
    mst_edges, _ = kruskal_mst(edges, n)
    return set(mst_edges) == set(given_mst)

# Test Case 1
n = 4
m = 5
edges = [(0, 1, 10),(0, 2, 6),(0, 3, 5),(1, 3, 15),(2, 3, 4)]
given_mst = [(2, 3, 4), (0, 3, 5), (0, 1, 10)]

is_unique = is_unique_mst(edges, n, given_mst)
print("Is the given MST unique?", is_unique)
