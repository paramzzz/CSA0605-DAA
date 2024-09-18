def max_degree_vertex_cover(edges, n):
    # Create an adjacency list representation of the graph
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Initialize the vertex cover and the set of uncovered edges
    vertex_cover = []
    uncovered_edges = set(edges)

    # Greedily select vertices to add to the vertex cover based on the maximum degree heuristic
    while uncovered_edges:
        # Find the vertex with the maximum degree
        max_degree_vertex = max(range(n), key=lambda x: len(graph[x]))

        # Add the vertex to the vertex cover
        vertex_cover.append(max_degree_vertex)

        # Remove edges incident to the vertex from the set of uncovered edges
        for neighbor in graph[max_degree_vertex]:
            uncovered_edges.discard((max_degree_vertex, neighbor))
            uncovered_edges.discard((neighbor, max_degree_vertex))

        # Remove the vertex from the graph
        graph[max_degree_vertex] = []

    return vertex_cover

# Test Case 1
n = 6
m = 7
edges = [(0, 1),(0, 2),(1, 3),(1, 4),(2, 4),(3, 5),(4, 5)]

vertex_cover = max_degree_vertex_cover(edges, n)
print("Vertex Cover:", vertex_cover)
