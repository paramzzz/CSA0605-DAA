import sys
import heapq

def dijkstra(edges, n, source, target):
    
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))

    distances = [sys.maxsize] * n
    distances[source] = 0

    pq = [(0, source)]

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_vertex == target:
            return current_distance

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return -1


n = 6
edges = [(0, 1, 7), (0, 2, 9), (0, 5, 14), (1, 2, 10), (1, 3, 15),
         (2, 3, 11), (2, 5, 2), (3, 4, 6), (4, 5, 9)]
source = 0
target = 4
print("The shortest distance from the source vertex to the target vertex is:", dijkstra(edges, n, source, target))
