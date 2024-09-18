def obst(keys, freq):
    n = len(keys)
    cost = [[0] * n for _ in range(n)]
    root = [[0] * n for _ in range(n)]

    for i in range(n):
        cost[i][i] = freq[i]
        root[i][i] = i

    for L in range(1, n):
        for i in range(n - L):
            j = i + L
            cost[i][j] = float('inf')
            for r in range(i, j + 1):
                c = 0
                if i > 0:
                    c += cost[i - 1][r - 1]
                if j < n - 1:
                    c += cost[r + 1][j]
                c += sum(freq[i:j + 1])
                if c < cost[i][j]:
                    cost[i][j] = c
                    root[i][j] = r

    return cost, root

# Test Case 1:
keys = [10, 12, 16, 21]
freq = [4, 2, 6, 3]
cost, root = obst(keys, freq)
print("Cost Table:")
for i in range(len(keys)):
    for j in range(len(keys)):
        print(f"cost[{i}][{j}] = {cost[i][j]}", end=" ")
    print()
print(f"Root Matrix:")
for i in range(len(keys)):
    for j in range(len(keys)):
        print(f"root[{i}][{j}] = {root[i][j]}", end=" ")
    print()
print(f"Optimal Cost: {cost[0][len(keys) - 1]}")

