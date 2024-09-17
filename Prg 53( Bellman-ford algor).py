def catMouseGame(graph):
    n = len(graph)
    draw = [False] * n
    win = [False] * n
    for i in range(n - 1, -1, -1):
        if i != 0:
            for j in graph[i]:
                if j == 0:
                    win[i] = True
                elif not win[j]:
                    win[i] = True
                    break
            else:
                draw[i] = True
    if win[1]:
        return 1
    elif draw[1]:
        return 0
    else:
        return 2

print(catMouseGame([[2, 3], [3], [4], []]))  # Output: 1
print(catMouseGame([[2, 3, 4], [3, 4], [0, 4], []]))  # Output: 2
print(catMouseGame([[3, 4], [2, 4], [1, 4], []]))  # Output: 0
