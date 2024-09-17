def floyd_warshall(graph):
    
    num_vertices = len(graph)
    distance_matrix = list(map(lambda i: list(map(lambda j: j, i)), graph))

    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                distance_matrix[i][j] = min(distance_matrix[i][j], distance_matrix[i][k] + distance_matrix[k][j])

    return distance_matrix


def print_distance_matrix(matrix, title):
        print(title)
    for row in matrix:
        print(" ".join(str(x) for x in row))


def print_shortest_path(graph, distance_matrix, start, end):
    
    path = [start]
    current_vertex = start
    while current_vertex != end:
        for i in range(len(graph)):
            if graph[current_vertex][i] != 0 and distance_matrix[start][end] == distance_matrix[start][current_vertex] + distance_matrix[current_vertex][i]:
                path.append(i)
                current_vertex = i
                break
    print("Shortest path from vertex {} to vertex {}: {}".format(start, end, " -> ".join(str(x) for x in path)))



if __name__ == "__main__":
    graph = [
        [0, 5, 0, 10],
        [0, 0, 3, 0],
        [0, 0, 0, 1],
        [0, 0, 0, 0]
    ]

    print_distance_matrix(graph, "Original Distance Matrix:")
    distance_matrix = floyd_warshall(graph)
    print_distance_matrix(distance_matrix, "\nShortest Distance Matrix:")
    print_shortest_path(graph, distance_matrix, 0, 3)
