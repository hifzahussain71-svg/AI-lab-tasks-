
import heapq

graph = {
    "S": [("A", 1), ("B", 4)],
    "A": [("C", 2)],
    "B": [("G", 5)],
    "C": [("G", 3)],
    "G": []
}

def ucs(start, goal):

    pq = [(0, start, [start])]

    best_cost = {start: 0}

    processed = []
    expanded = []

    while pq:
        cost, node, path = heapq.heappop(pq)

        if cost != best_cost.get(node):
            continue

        processed.append((node, cost))

     
        if node == goal:
            return path, cost, processed, expanded

        expanded.append(node)

        for neighbor, weight in graph.get(node, []):

            new_cost = cost + weight

            if new_cost < best_cost.get(
                neighbor, float("inf")
            ):
                best_cost[neighbor] = new_cost

                heapq.heappush(
                    pq,
                    (new_cost, neighbor, path + [neighbor])
                )

    return None, float("inf"), processed, expanded



path, cost, processed, expanded = ucs("S", "G")

print("UCS Processing Order:")
print(processed)

print("\nExpanded Nodes:")
print(expanded)

print("\nExpansion Count:")
print(len(expanded))

print("\nFinal Path:")
print(path)

print("\nTotal Path Cost:")
print(cost)
