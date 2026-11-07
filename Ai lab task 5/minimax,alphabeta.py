
tree = [
    [[3, 5], [6, 9]],
    [[1, 2], [0, -1]]
]

minimax_count = 0
alphabeta_count = 0


def minimax(node, maximizing):
    global minimax_count

    if isinstance(node, int):
        minimax_count += 1
        return node

    values = []

    for child in node:
        values.append(minimax(child, not maximizing))

    if maximizing:
        return max(values)
    else:
        return min(values)


def alpha_beta(node, alpha, beta, maximizing):
    global alphabeta_count

    if isinstance(node, int):
        alphabeta_count += 1
        return node

    if maximizing:
        value = float('-inf')

        for child in node:
            value = max(
                value,
                alpha_beta(child, alpha, beta, False)
            )

            alpha = max(alpha, value)

            if alpha >= beta:
                break

        return value

    else:
        value = float('inf')

        for child in node:
            value = min(
                value,
                alpha_beta(child, alpha, beta, True)
            )

            beta = min(beta, value)

            if alpha >= beta:
                break

        return value


minimax_count = 0
alphabeta_count = 0

minimax_value = minimax(tree, True)

alphabeta_value = alpha_beta(
    tree,
    float('-inf'),
    float('inf'),
    True
)

print("ORIGINAL TREE")
print("Minimax Value:", minimax_value)
print("Alpha-Beta Value:", alphabeta_value)
print("Minimax Leaves:", minimax_count)
print("Alpha-Beta Leaves:", alphabeta_count)

reordered_tree = [
    [[-1, 0], [2, 1]],
    [[9, 6], [5, 3]]
]

minimax_count = 0
alphabeta_count = 0

minimax_value2 = minimax(reordered_tree, True)

alphabeta_value2 = alpha_beta(
    reordered_tree,
    float('-inf'),
    float('inf'),
    True
)

print("\nREORDERED TREE")
print("Minimax Value:", minimax_value2)
print("Alpha-Beta Value:", alphabeta_value2)
print("Minimax Leaves:", minimax_count)
print("Alpha-Beta Leaves:", alphabeta_count)
