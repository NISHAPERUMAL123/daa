"""
Experiment 8: Travelling Salesman Problem using Branch and Bound for
Finding Optimal Path

Uses a priority queue (best-first search) where each node is a partial
tour. A lower bound is computed for each partial tour (sum of two cheapest
edges per unvisited city / 2), and branches whose bound exceeds the current
best solution are pruned.

Time Complexity: O(N! ) worst case, but bounding prunes large portions of
                  the search tree in practice
Space Complexity: O(N^2) for the cost matrix + O(N) per queue node
"""

import heapq


class Node:
    def __init__(self, level, path, bound, cost):
        self.level = level
        self.path = path
        self.bound = bound
        self.cost = cost

    def __lt__(self, other):
        return self.bound < other.bound


def calculate_bound(graph, path, n):
    # Standard lower bound: for every vertex, sum its two cheapest edges,
    # then halve the total (each edge is counted from both its endpoints).
    total = 0
    for i in range(n):
        row = sorted(graph[i][j] for j in range(n) if j != i)
        if len(row) >= 2:
            total += row[0] + row[1]
        elif len(row) == 1:
            total += row[0] * 2
    return total / 2


def tsp_branch_and_bound(graph, n):
    pq = []
    root = Node(0, [0], calculate_bound(graph, [0], n), 0)
    heapq.heappush(pq, root)

    best_cost = float("inf")
    best_path = None

    while pq:
        node = heapq.heappop(pq)

        if node.bound >= best_cost:
            continue

        if node.level == n - 1:
            last, first = node.path[-1], node.path[0]
            if graph[last][first] != float("inf"):
                total_cost = node.cost + graph[last][first]
                if total_cost < best_cost:
                    best_cost = total_cost
                    best_path = node.path + [first]
            continue

        for city in range(n):
            if city not in node.path and graph[node.path[-1]][city] != float("inf"):
                new_path = node.path + [city]
                new_cost = node.cost + graph[node.path[-1]][city]
                new_bound = calculate_bound(graph, new_path, n)
                if new_bound < best_cost:
                    heapq.heappush(pq, Node(node.level + 1, new_path, new_bound, new_cost))

    return best_path, best_cost


if __name__ == "__main__":
    INF = float("inf")
    graph = [
        [INF, 10, 15, 20],
        [10, INF, 35, 25],
        [15, 35, INF, 30],
        [20, 25, 30, INF],
    ]
    n = len(graph)

    print("Distance matrix:")
    for row in graph:
        print(" ", ["INF" if x == INF else x for x in row])
    print()

    best_path, best_cost = tsp_branch_and_bound(graph, n)
    print(f"Optimal path: {' -> '.join(map(str, best_path))}")
    print(f"Minimum cost: {best_cost}")
