import heapq

def maxProbability(n, edges, succProb, start, end):
    graph = [[] for _ in range(n)]
    for i, (a, b) in enumerate(edges):
        graph[a].append((b, succProb[i]))
        graph[b].append((a, succProb[i]))

    pq = [(-1, start)]
    prob = [0] * n
    prob[start] = 1

    while pq:
        p, node = heapq.heappop(pq)
        p = -p
        if p < prob[node]:
            continue
        for neighbor, edge_prob in graph[node]:
            new_prob = p * edge_prob
            if new_prob > prob[neighbor]:
                prob[neighbor] = new_prob
                heapq.heappush(pq, (-new_prob, neighbor))

    return prob[end]

print(maxProbability(3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.2], 0, 2))  # Output: 0.25
print(maxProbability(3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.3], 0, 2))  # Output: 0.3
print(maxProbability(3, [[0,1]], [0.5], 0, 2))  # Output: 0.0
