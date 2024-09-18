import matplotlib.pyplot as plt
import numpy as np

def visualize_n_queens(n, solution):
    fig, ax = plt.subplots()
    ax.set_xlim(0, n)
    ax.set_ylim(0, n)
    ax.set_xticks(np.arange(n))
    ax.set_yticks(np.arange(n))
    ax.grid(True)
    for i in range(n):
        for j in range(n):
            if (i, j) in solution:
                ax.plot(j, i, 'ro')  # Red circle for queen
            else:
                ax.plot(j, i, 'bo')  # Blue circle for empty space
    plt.show()

n = 4
solution = [(0, 1), (1, 3), (2, 0), (3, 2)]  # One possible solution for 4-Queens
visualize_n_queens(n, solution)
