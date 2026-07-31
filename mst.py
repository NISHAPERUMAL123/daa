"""
Experiment 3: Implementation of Kruskal's and Prim's Algorithms for
Minimum Spanning Tree (MST)

Kruskal's Algorithm : Greedy, edge-based, uses Union-Find (Disjoint Set)
                       Time Complexity: O(E log E)
Prim's Algorithm    : Greedy, vertex-based, uses a Min-Heap
                       Time Complexity: O(E log V)
"""

import heapq


class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_y] = root_x
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1
        return True


def kruskal_mst(num_vertices, edges):
    """edges: list of (weight, u, v)"""
    edges = sorted(edges)
    ds = DisjointSet(num_vertices)
    mst_edges = []
    total_weight = 0

    for weight, u, v in edges:
        if ds.union(u, v):
            mst_edges.append((u, v, weight))
            total_weight += weight
            if len(mst_edges) == num_vertices - 1:
                break

    return mst_edges, total_weight


def prim_mst(num_vertices, adj):
    """adj: dict {vertex: [(neighbor, weight), ...]}"""
    visited = [False] * num_vertices
    min_heap = [(0, 0, -1)]  # (weight, vertex, parent)
    mst_edges = []
    total_weight = 0

    while min_heap and len(mst_edges) < num_vertices:
        weight, u, parent = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        if parent != -1:
            mst_edges.append((parent, u, weight))
            total_weight += weight

        for v, w in adj[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v, u))

    return mst_edges, total_weight


if __name__ == "__main__":
    # Sample graph: 5 vertices (0-4)
    num_vertices = 5
    edge_list = [
        (2, 0, 1), (3, 0, 3), (3, 1, 2),
        (4, 1, 3), (1, 2, 3), (2, 3, 4), (6, 2, 4)
    ]  # (weight, u, v)

    print("Graph edges (weight, u, v):", edge_list, "\n")

    mst_edges, total_weight = kruskal_mst(num_vertices, edge_list)
    print("Kruskal's MST:")
    for u, v, w in mst_edges:
        print(f"  {u} -- {v} (weight {w})")
    print(f"  Total weight: {total_weight}\n")

    adjacency = {i: [] for i in range(num_vertices)}
    for weight, u, v in edge_list:
        adjacency[u].append((v, weight))
        adjacency[v].append((u, weight))

    mst_edges, total_weight = prim_mst(num_vertices, adjacency)
    print("Prim's MST:")
    for u, v, w in mst_edges:
        print(f"  {u} -- {v} (weight {w})")
    print(f"  Total weight: {total_weight}")
