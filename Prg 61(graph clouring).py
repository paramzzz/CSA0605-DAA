def graph_coloring(graph):
    
    colors = {}
    for vertex in graph:
        available_colors = set(range(1, len(graph) + 1))
        for neighbor in graph[vertex]:
            if neighbor in colors:
                available_colors.discard(colors[neighbor])
        colors[vertex] = min(available_colors)
    return colors


def max_regions(graph):
    
    
    colors = graph_coloring(graph)
    max_color = max(colors.values())
    first_person_colors = sum(1 for color in colors.values() if color == 1)
    return first_person_colors


def print_graph(graph):
    
    
    for vertex in graph:
        print(vertex, "->", graph[vertex])



if __name__ == "__main__":
    
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D'],
        'D': ['B', 'C', 'E'],
        'E': ['D']
    }

    print("Adjacency List Representation of the Graph:")
    print_graph(graph)
