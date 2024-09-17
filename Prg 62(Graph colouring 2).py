def graph_coloring(edges, n, k):
    
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    colors = {}

    def assign_colors(vertex, color):
        available_colors = set(range(1, k + 1))
        for neighbor in graph[vertex]:
            if neighbor in colors:
                available_colors.discard(colors[neighbor])
        colors[vertex] = min(available_colors)

    for vertex in range(n):
        assign_colors(vertex, 1)

    max_regions = sum(1 for color in colors.values() if color == 1)

    return max_regions


edges = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)]
n = 4
k = 3

print("Maximum Number of Regions Colored by the First Person:", graph_coloring(edges, n, k))

