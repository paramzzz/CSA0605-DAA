def count_ways(m, n, N, i, j):
    """
    Function to count the number of ways to move the ball out of the grid boundary in exactly N steps.

    Args:
    m (int): The number of rows in the grid.
    n (int): The number of columns in the grid.
    N (int): The exact number of steps.
    i (int): The starting row index.
    j (int): The starting column index.

    Returns:
    int: The number of ways to move the ball out of the grid boundary in exactly N steps.
    """
    # Initialize a 3D DP table to store the number of ways
    dp = [[[0 for _ in range(N + 1)] for _ in range(n)] for _ in range(m)]

    # Base case: If the ball is already out of the grid, there is 1 way
    for x in range(m):
        for y in range(n):
            dp[x][y][0] = 1

    # Fill up the DP table
    for k in range(1, N + 1):
        for x in range(m):
            for y in range(n):
                # Move up
                if x > 0:
                    dp[x][y][k] += dp[x - 1][y][k - 1]
                # Move down
                if x < m - 1:
                    dp[x][y][k] += dp[x + 1][y][k - 1]
                # Move left
                if y > 0:
                    dp[x][y][k] += dp[x][y - 1][k - 1]
                # Move right
                if y < n - 1:
                    dp[x][y][k] += dp[x][y + 1][k - 1]

    # Count the number of ways to move out of the grid boundary
    ways = 0
    for x in range(m):
        ways += dp[x][0][N] + dp[x][n - 1][N]
    for y in range(n):
        ways += dp[0][y][N] + dp[m - 1][y][N]

    return ways


# Example usage
m = 2
n = 2
N = 2
i = 0
j = 0
print("Number of ways to move out of the grid boundary in exactly", N, "steps:", count_ways(m, n, N, i, j))
