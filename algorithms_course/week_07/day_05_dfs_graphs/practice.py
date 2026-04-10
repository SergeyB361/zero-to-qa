# Неделя 7, День 5 - DFS по графу
#
# Задание 1:
# Реализуй dfs_order(graph, start).
#
# Задание 2:
# Реализуй reachable_dfs(graph, start, target).
#
# Задание 3:
# Реализуй connected_component(graph, start),
# которая возвращает множество достижимых вершин.


def dfs_order(graph: dict[str, list[str]], start: str) -> list[str]:
    return []



def reachable_dfs(graph: dict[str, list[str]], start: str, target: str) -> bool:
    return False



def connected_component(graph: dict[str, list[str]], start: str) -> set[str]:
    return set()


if __name__ == "__main__":
    graph = {"A": ["B", "C"], "B": ["D"], "C": [], "D": []}
    print(dfs_order(graph, "A"))
    print(reachable_dfs(graph, "A", "D"))
    print(connected_component(graph, "A"))
    print("Реализуй DFS и связанные функции.")
