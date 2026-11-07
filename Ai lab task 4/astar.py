
import heapq
graph = {
    "S": [("A", 1), ("B", 4)],
    "A": [("C", 2)],
    "B": [("G", 5)],
    "C": [("G", 3)],
    "G": []
}
h = {
    "S": 5,
    "A": 4,
    "B": 4,
    "C": 2,
    "G": 0
}
def astar(graph, h, start, goal):
    pq = [(h[start], 0, start, [start])]
    best = {start: 0}
    processed = []
    expanded = []
    while pq:
        f, g, node, path = heapq.heappop(pq)

        if g != best.get(node):
            continue

        processed.append((node, g, h[node], f))

        if node == goal:
            return path, g, processed, expanded

        expanded.append(node)

        for nxt, w in graph.get(node, []):
            ng = g + w

            if ng < best.get(nxt, float("inf")):
                best[nxt] = ng

                heapq.heappush(
                    pq,
                    (ng + h[nxt], ng, nxt, path + [nxt])
                )

    return None, float("inf"), processed, expanded

path, cost, processed, expanded = astar(
    graph, h, "S", "G"
)

print("Path:", path)
print("Cost:", cost)
print("Processed:", processed)
print("Expanded:", expanded)
print("Expansion count:", len(expanded))
