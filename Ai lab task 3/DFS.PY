
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}
def dfs(start, goal):
    stack = [(start, [start])]
    seen = set()
    while stack:
        node, path = stack.pop()
        if node in seen:
            continue
        seen.add(node)
        if node == goal:
            return path
        for n in reversed(graph[node]):
            if n not in seen:
                stack.append((n, path + [n]))
    return None
print(dfs("A", "G"))
