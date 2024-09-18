import sys
import heapq

def prim_mst(graph):
    
    mst = []

    start_node = next(iter(graph))

    queue = [(0, start_node, None)] 

    visited = set()

    while queue:
        cost, node, parent = heapq.heappop(queue)

        if node in visited:
            continue

        visited.add(node)

        if parent is not None:
            mst.append((parent, node, cost))

        for neighbor, edge_cost in graph[node].items():
            if neighbor not in visited:
                heapq.heappush(queue, (edge_cost, neighbor, node))

    return mst

graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 4},
    'C': {'A': 3, 'B': 1, 'D': 5},
    'D': {'B': 4, 'C': 5}
}

mst = prim_mst(graph)

print("Minimum Cost Spanning Tree:")
for edge in mst:
    print(f"{edge[0]} --{edge[2]}--> {edge[1]}")
