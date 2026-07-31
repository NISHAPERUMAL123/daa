"""
Experiment 7: Solving N-Queens Problem using Backtracking

Place N queens on an N x N chessboard such that no two queens attack each
other (no shared row, column, or diagonal). Backtracking incrementally
builds the solution column by column, pruning invalid branches early.

Time Complexity: O(N!) worst case (heavily pruned in practice)
Space Complexity: O(N^2) for the board, O(N) for recursion
"""


def is_safe(board, row, col, n):
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens_util(board, col, n, solutions):
    if col >= n:
        solutions.append(["".join("Q" if cell else "." for cell in row) for row in board])
        return

    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens_util(board, col + 1, n, solutions)
            board[row][col] = 0  # backtrack


def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]
    solutions = []
    solve_n_queens_util(board, 0, n, solutions)
    return solutions


if __name__ == "__main__":
    n = 8
    solutions = solve_n_queens(n)

    print(f"N-Queens for N = {n}")
    print(f"Total solutions found: {len(solutions)}\n")

    print("First solution:")
    for row in solutions[0]:
        print(" ", row)
