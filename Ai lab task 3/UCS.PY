
import heapq
weighted_graph = {
    "A": [("B", 1), ("C", 4)],
    "B": [("D", 2), ("E", 1)],
    "C": [("F", 3), ("G", 8)],
    "D": [],
    "E": [("G", 1)],
    "F": [],
    "G": []
}

def ucs(start, goal):
    frontier = [(0, start, [start])]
    best_cost = {start: 0}
    processed = []

    while frontier:
        cost, node, path = heapq.heappop(frontier)

        if cost != best_cost.get(node):
            continue

        processed.append((node, cost))

        if node == goal:
            return path, cost, processed

        for child, weight in weighted_graph[node]:
            new_cost = cost + weight

            if new_cost < best_cost.get(child, float("inf")):
                best_cost[child] = new_cost
                heapq.heappush(
                    frontier,
                    (new_cost, child, path + [child])
                )

    return None, float("inf"), processed

path, cost, order = ucs("A", "G")

print("UCS Path:", path)
print("Total Cost:", cost)
print("Processing Order:", order)
