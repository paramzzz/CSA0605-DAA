import sys

def dijkstra(graph, source):
    
    distances = [sys.maxsize] * len(graph)
    distances[source] = 0

    unvisited = set(range(len(graph)))

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        unvisited.remove(current_vertex)

        for neighbor, weight in enumerate(graph[current_vertex]):
            if weight != sys.maxsize and distances[current_vertex] + weight < distances[neighbor]:
                distances[neighbor] = distances[current_vertex] + weight

    return distances


n = 5
graph = [[0, 10, 3, float('inf'), float('inf')],
         [float('inf'), 0, 1, 2, float('inf')],
         [float('inf'), 4, 0, 8, 2],
         [float('inf'), float('inf'), float('inf'), 0, 7],
         [float('inf'), float('inf'), float('inf'), 9, 0]]
source = 0
print("The shortest distances from the source vertex are:", dijkstra(graph, source))
