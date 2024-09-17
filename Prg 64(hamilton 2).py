def has_hamiltonian_cycle(edges, n):
    """
    Function to detect if a Hamiltonian cycle exists in an undirected graph.

    Args:
    edges (list): List of edges in the graph.
    n (int): Number of vertices in the graph.

    Returns:
    bool: True if a Hamiltonian cycle exists, False otherwise.
    """
    # Create an adjacency list representation of the graph
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Function to perform DFS
    def dfs(vertex, path, visited):
        if len(path) == n:
            if path[0] in graph[path[-1]]:
                return True
            return False
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                path.append(neighbor)
                if dfs(neighbor, path, visited):
                    return True
                path.pop()
                visited.remove(neighbor)
        return False

    # Perform DFS from each vertex
    for vertex in range(n):
        if dfs(vertex, [vertex], {vertex}):
            return True

    return False


# Example usage
edges = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)]
n = 4

print("Does a Hamiltonian cycle exist?", has_hamiltonian_cycle(edges, n))
