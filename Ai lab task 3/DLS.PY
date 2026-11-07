
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}

FOUND = "FOUND"
CUTOFF = "CUTOFF"
FAILURE = "FAILURE"

def dls(start, goal, limit):
    processed = []
    path = [start]

    def visit(node, depth):
        processed.append(node)

        if node == goal:
            return FOUND

        if depth == limit:
            if graph[node]:
                return CUTOFF
            return FAILURE

        cutoff_occurred = False

        for child in graph[node]:
            if child in path:
                continue

            path.append(child)
            result = visit(child, depth + 1)

            if result == FOUND:
                return FOUND

            path.pop()

            if result == CUTOFF:
                cutoff_occurred = True

        if cutoff_occurred:
            return CUTOFF

        return FAILURE

    status = visit(start, 0)

    return status, path[:] if status == FOUND else None, processed

for limit in range(1, 5):
    status, path, order = dls("A", "G", limit)

    print("Limit:", limit)
    print("Status:", status)
    print("Path:", path)
    print("Processed:", order)
    print()
