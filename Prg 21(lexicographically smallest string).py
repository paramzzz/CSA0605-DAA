class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y

def smallestStringWithSwaps(s: str, pairs: list[list[int]]) -> str:
    n = len(s)
    uf = UnionFind(n)
    for x, y in pairs:
        uf.union(x, y)

    groups = {}
    for i in range(n):
        root = uf.find(i)
        if root not in groups:
            groups[root] = []
        groups[root].append(i)

    res = list(s)
    for indices in groups.values():
        chars = [s[i] for i in indices]
        chars.sort()
        for i, c in zip(indices, chars):
            res[i] = c

    return ''.join(res)
s = "dcab"
pairs = [[0, 3], [1, 2]]
print(smallestStringWithSwaps(s, pairs))  # Output: "bacd"
