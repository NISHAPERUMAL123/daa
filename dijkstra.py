"""
Experiment 4: Implementation of Single Source Shortest Path Algorithm
(Dijkstra's Algorithm)

Uses a min-heap (priority queue) to always expand the closest unvisited
vertex, relaxing edges as it goes.

Time Complexity: O((V + E) log V) using a binary heap
Space Complexity: O(V + E)

Note: Works only for graphs with non-negative edge weights.
"""

import heapq


def dijkstra(num_vertices, adj, source):
    """adj: dict {vertex: [(neighbor, weight), ...]}"""
    dist = [float("inf")] * num_vertices
    dist[source] = 0
    prev = [-1] * num_vertices
    visited = [False] * num_vertices

    min_heap = [(0, source)]

    while min_heap:
        d, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True

        for v, weight in adj[u]:
            if not visited[v] and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                prev[v] = u
                heapq.heappush(min_heap, (dist[v], v))

    return dist, prev


def get_path(prev, target):
    path = []
    while target != -1:
        path.append(target)
        target = prev[target]
    return path[::-1]


if __name__ == "__main__":
    num_vertices = 6
    edge_list = [
        (0, 1, 4), (0, 2, 2), (1, 2, 1),
        (1, 3, 5), (2, 3, 8), (2, 4, 10),
        (3, 4, 2), (3, 5, 6), (4, 5, 3)
    ]  # (u, v, weight)

    adjacency = {i: [] for i in range(num_vertices)}
    for u, v, w in edge_list:
        adjacency[u].append((v, w))
        adjacency[v].append((u, w))

    source = 0
    dist, prev = dijkstra(num_vertices, adjacency, source)

    print(f"Shortest distances from vertex {source}:")
    for v in range(num_vertices):
        path = get_path(prev, v)
        print(f"  To {v}: distance = {dist[v]:<5} path = {' -> '.join(map(str, path))}")
