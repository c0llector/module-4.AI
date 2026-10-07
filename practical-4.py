tree = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": ["H", "I"],
    "E": ["J", "K"],
    "F": ["L", "M"],
    "G": ["N", "O"]
}

payoffs = {
    "H": 4,
    "I": 9,
    "J": 7,
    "K": 2,
    "L": 3,
    "M": 8,
    "N": 6,
    "O": 1
}


def is_terminal(state):
    return state in payoffs


def successors(state, reverse=False):
    children = tree[state]
    return list(reversed(children)) if reverse else children


def utility(state):
    return payoffs[state]


def minimax(state, maximizing, counter, reverse=False):
    counter[0] += 1

    if is_terminal(state):
        return utility(state)

    value = float("-inf") if maximizing else float("inf")

    for child in successors(state, reverse):
        child_value = minimax(
            child, not maximizing, counter, reverse
        )

        if maximizing:
            value = max(value, child_value)
        else:
            value = min(value, child_value)

    return value


def alphabeta(
    state, alpha, beta, maximizing,
    counter, visited, pruned, reverse=False
):
    counter[0] += 1
    visited.append(state)

    if is_terminal(state):
        return utility(state)

    children = successors(state, reverse)
    value = float("-inf") if maximizing else float("inf")

    for index, child in enumerate(children):
        child_value = alphabeta(
            child, alpha, beta, not maximizing,
            counter, visited, pruned, reverse
        )

        if maximizing:
            value = max(value, child_value)
            alpha = max(alpha, value)
        else:
            value = min(value, child_value)
            beta = min(beta, value)

        if alpha >= beta:
            pruned.extend(children[index + 1:])
            break

    return value


def main():
    for reverse in (False, True):
        mm_calls = [0]
        ab_calls = [0]
        visited = []
        pruned = []

        mm_value = minimax(
            "A", True, mm_calls, reverse
        )

        ab_value = alphabeta(
            "A", float("-inf"), float("inf"), True,
            ab_calls, visited, pruned, reverse
        )

        print(
            "\nБағыт:",
            "Оңнан солға" if reverse else "Солдан оңға"
        )
        print("Minimax мәні:", mm_value)
        print("Minimax шақырулары:", mm_calls[0])
        print("Alpha–Beta мәні:", ab_value)
        print("Alpha–Beta шақырулары:", ab_calls[0])
        print("Қаралған түйіндер:", " -> ".join(visited))
        print(
            "Қиылған жапырақтар:",
            ", ".join(pruned) if pruned else "Жоқ"
        )

        assert mm_value == ab_value


if __name__ == "__main__":
    main()