# Неделя 7, День 6 - Практика на графы
#
# Задание 1:
# Реализуй node_count(graph).
#
# Задание 2:
# Реализуй edge_count_directed(graph).
#
# Задание 3:
# Реализуй shortest_reach(graph, start) через BFS,
# возвращающую dict вершина -> расстояние.


from collections import deque



def node_count(graph: dict[str, list[str]]) -> int:
    return -1



def edge_count_directed(graph: dict[str, list[str]]) -> int:
    return -1



def shortest_reach(graph: dict[str, list[str]], start: str) -> dict[str, int]:
    return {}


if __name__ == "__main__":
    graph = {"A": ["B", "C"], "B": ["D"], "C": [], "D": []}
    print(node_count(graph))
    print(edge_count_directed(graph))
    print(shortest_reach(graph, "A"))
    print("Ожидается: node_count = 4, edge_count_directed = 3, shortest_reach = {'A': 0, 'B': 1, 'C': 1, 'D': 2}")
    print("Реализуй mixed practice по графам.")
