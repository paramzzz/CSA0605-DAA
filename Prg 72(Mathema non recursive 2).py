def unique_paths(m, n):
    
    paths = [[0] * n for _ in range(m)]

    for i in range(m):
        paths[i][0] = 1
    for j in range(n):
        paths[0][j] = 1

    for i in range(1, m):
        for j in range(1, n):
            paths[i][j] = paths[i-1][j] + paths[i][j-1]

    return paths[m-1][n-1]


m = 7
n = 3
print("Number of unique paths:", unique_paths(m, n))
