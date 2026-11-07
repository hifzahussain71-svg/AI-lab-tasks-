
def iddfs(start, goal, max_depth):
    all_orders = []

    for limit in range(1, max_depth + 1):
        status, path, order = dls(start, goal, limit)

        all_orders.append((limit, status, path, order))

        if status == FOUND:
            return status, path, all_orders

    return CUTOFF, None, all_orders


for maximum in range(1, 5):
    status, path, runs = iddfs("A", "G", maximum)

    print("Maximum Depth:", maximum)
    print("Status:", status)
    print("Path:", path)
    print("Limits Attempted:", [r[0] for r in runs])
    print()
