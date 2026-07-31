"""
Experiment 6: Optimal Cost Computation in Matrix Chain Multiplication
using Dynamic Programming Technique

Given a chain of matrices, find the most efficient way (minimum number of
scalar multiplications) to multiply them, by choosing the optimal
parenthesization.

Time Complexity: O(n^3)
Space Complexity: O(n^2)
"""


def matrix_chain_order(dims):
    """
    dims: list of matrix dimensions such that matrix i has
          dimensions dims[i-1] x dims[i]
    Returns: (min cost, DP table, split table)
    """
    n = len(dims) - 1  # number of matrices
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    split = [[0] * (n + 1) for _ in range(n + 1)]

    # length is the chain length being solved
    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            dp[i][j] = float("inf")
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + dims[i - 1] * dims[k] * dims[j]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    split[i][j] = k

    return dp[1][n], dp, split


def print_optimal_parens(split, i, j):
    if i == j:
        return f"M{i}"
    else:
        k = split[i][j]
        left = print_optimal_parens(split, i, k)
        right = print_optimal_parens(split, k + 1, j)
        return f"({left} x {right})"


if __name__ == "__main__":
    # Example: matrices of dims 40x20, 20x30, 30x10, 10x30
    dims = [40, 20, 30, 10, 30]
    n = len(dims) - 1

    min_cost, dp, split = matrix_chain_order(dims)

    print(f"Matrix dimensions (p0..pn): {dims}")
    print(f"Number of matrices: {n}\n")

    print(f"Minimum number of scalar multiplications: {min_cost}")
    print(f"Optimal parenthesization: {print_optimal_parens(split, 1, n)}")
