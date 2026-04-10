# Неделя 2, День 7 - Мини-проект: Route Finder


def reachable(graph: dict[str, list[str]], start: str, target: str) -> bool:
    return False


def shortest_distance(graph: dict[str, list[str]], start: str, target: str) -> int:
    return -1


def restore_path(graph: dict[str, list[str]], start: str, target: str) -> list[str]:
    return []


def main() -> None:
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['E'],
        'D': ['F'],
        'E': [],
        'F': [],
    }

    print('Route Finder demo scaffold')
    print('reachable(A, F) ->', reachable(graph, 'A', 'F'), '| expected: True')
    print('shortest_distance(A, F) ->', shortest_distance(graph, 'A', 'F'), '| expected: 3')
    print("restore_path(A, F) ->", restore_path(graph, 'A', 'F'), "| expected: ['A', 'B', 'D', 'F']")


if __name__ == "__main__":
    main()
