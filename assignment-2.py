tree = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": ["H", "I"],
    "E": ["J", "K"],
    "F": ["L", "M"],
    "G": ["N", "O"],
}

utility = {
    "H": 3,
    "I": 12,
    "J": 8,
    "K": 2,
    "L": 4,
    "M": 6,
    "N": 14,
    "O": 5,
}


def minimax(node, maximizing, reverse=False, visited=None):
    if visited is None:
        visited = []

    visited.append(node)

    if node in utility:
        return utility[node], None

    children = tree[node]
    if reverse:
        children = children[::-1]

    best_value = float("-inf") if maximizing else float("inf")
    best_move = None

    for child in children:
        value, _ = minimax(
            child, not maximizing, reverse, visited
        )

        if maximizing:
            if value > best_value:
                best_value = value
                best_move = child
        else:
            if value < best_value:
                best_value = value
                best_move = child

    return best_value, best_move 


def alphabeta(
    node,
    maximizing,
    alpha=float("-inf"),
    beta=float("inf"),
    reverse=False,
    visited=None,
):
    if visited is None:
        visited = []

    visited.append(node)

    if node in utility:
        return utility[node], None

    children = tree[node]
    if reverse:
        children = children[::-1]

    best_value = float("-inf") if maximizing else float("inf")
    best_move = None

    for child in children:
        value, _ = alphabeta(
            child, not maximizing,
            alpha, beta, reverse, visited
        )

        if maximizing:
            if value > best_value:
                best_value = value
                best_move = child

            alpha = max(alpha, best_value)

        else:
            if value < best_value:
                best_value = value
                best_move = child

            beta = min(beta, best_value)

        if alpha >= beta:
            break

    return best_value, best_move


for reverse in (False, True):
    direction = "Оңнан солға" if reverse else "Солдан оңға"

    mm_visited = []
    ab_visited = []

    mm_value, mm_move = minimax(
        "A", True, reverse=reverse, visited=mm_visited
    )

    ab_value, ab_move = alphabeta(
        "A", True, reverse=reverse, visited=ab_visited
    )

    print("\nБағыт:", direction)

    print(
        "Minimax:",
        "мән =", mm_value,
        "жүріс =", mm_move,
        "түйін =", len(mm_visited),
    )

    print(
        "Alpha-beta:",
        "мән =", ab_value,
        "жүріс =", ab_move,
        "түйін =", len(ab_visited),
    )

    print("Minimax реті:", " → ".join(mm_visited))
    print("Alpha-beta реті:", " → ".join(ab_visited))

    print(
        "Қиылған түйін саны:",
        len(mm_visited) - len(ab_visited)
    )
    

    print(
        "Шешім бірдей ме?",
        (mm_value, mm_move) == (ab_value, ab_move)
    )