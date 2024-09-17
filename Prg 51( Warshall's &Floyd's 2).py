import heapq

def findCity(n, edges, distanceThreshold):
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    def dijkstra(start):
        dist = [float('inf')] * n
        dist[start] = 0
        pq = [(0, start)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w in graph[u]:
                if dist[u] + w <= distanceThreshold and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))
        return sum(d <= distanceThreshold for d in dist)

    res = 0
    max_reachable = 0
    for i in range(n - 1, -1, -1):
        reachable = dijkstra(i)
        if reachable > max_reachable:
            max_reachable = reachable
            res = i
    return res

print(findCity(4, [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], 4))  # Output: 3
print(findCity(5, [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 3, 2], [2, 3, 1], [3, 4, 1]], 2))  # Output: 0
