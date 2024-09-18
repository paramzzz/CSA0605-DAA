def solve_n_queens(rows, cols):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or \
                board[i] - i == col - row or \
                board[i] + i == col + row:
                return False
        return True

    def place_queens(n, board, row):
        if row == n:
            return [board[:]]
        solutions = []
        for col in range(cols):
            if is_safe(board, row, col):
                board[row] = col
                solutions.extend(place_queens(n, board, row + 1))
        return solutions

    n = rows
    board = [-1] * n
    solutions = place_queens(n, board, 0)
    return solutions

rows, cols = 8, 10
solutions = solve_n_queens(rows, cols)
print("Possible solutions for 8x10 board:")
for solution in solutions:
    print(solution)
