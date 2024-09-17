import heapq

def networkDelayTime(times, n, k):
    graph = [[] for _ in range(n + 1)]
    for u, v, w in times:
        graph[u].append((v, w))

    def dijkstra(start):
        dist = [float('inf')] * (n + 1)
        dist[start] = 0
        pq = [(0, start)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))
        return max(dist[1:])

    return dijkstra(k) if dijkstra(k) != float('inf') else -1

print(networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))  # Output: 2
print(networkDelayTime([[1, 2, 1], [2, 3, 2], [1, 3, 2]], 3, 2))  # Output: -1
