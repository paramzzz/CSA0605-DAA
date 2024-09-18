def greedy_vertex_cover(edges, n):

    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    vertex_cover = []
    uncovered_edges = set(edges)

    while uncovered_edges:
        max_uncovered_edge = max(uncovered_edges, key=lambda x: len([edge for edge in uncovered_edges if x[0] in edge or x[1] in edge]))

        vertex_cover.append(max_uncovered_edge[0])

        for edge in list(uncovered_edges):
            if max_uncovered_edge[0] in edge:
                uncovered_edges.remove(edge)

    return vertex_cover

n = 5
m = 6
edges = [(0, 1),(0, 2),(1, 2),(1, 3),(2, 4),(3, 4)]

vertex_cover = greedy_vertex_cover(edges, n)
print("Vertex Cover:", vertex_cover)
