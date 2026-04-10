# Неделя 2, День 4 - BFS
#
# Задание 1:
# Реализуй bfs_order(graph, start).
#
# Задание 2:
# Реализуй reachable(graph, start, target) -> True/False.
#
# Задание 3:
# Реализуй bfs_levels(graph, start),
# которая возвращает dict вершина -> расстояние от start.


from collections import deque



def bfs_order(graph: dict[str, list[str]], start: str) -> list[str]:
    return []



def reachable(graph: dict[str, list[str]], start: str, target: str) -> bool:
    return False



def bfs_levels(graph: dict[str, list[str]], start: str) -> dict[str, int]:
    return {}


if __name__ == "__main__":
    graph = {"A": ["B", "C"], "B": ["D"], "C": [], "D": []}
    print(bfs_order(graph, "A"))
    print(reachable(graph, "A", "D"))
    print(bfs_levels(graph, "A"))
    print("Ожидается: bfs_order = ['A', 'B', 'C', 'D'], reachable = True, bfs_levels = {'A': 0, 'B': 1, 'C': 1, 'D': 2}")
    print("Реализуй BFS и связанные функции.")
