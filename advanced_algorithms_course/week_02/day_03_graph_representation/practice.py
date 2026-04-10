# Неделя 2, День 3 - Представление графа
#
# Задание 1:
# Реализуй build_directed_graph(edges).
#
# Задание 2:
# Реализуй build_undirected_graph(edges).
#
# Задание 3:
# Реализуй neighbors(graph, node) -> список соседей.


def build_directed_graph(edges: list[tuple[str, str]]) -> dict[str, list[str]]:
    return {}



def build_undirected_graph(edges: list[tuple[str, str]]) -> dict[str, list[str]]:
    return {}



def neighbors(graph: dict[str, list[str]], node: str) -> list[str]:
    return []


if __name__ == "__main__":
    edges = [("A", "B"), ("A", "C"), ("B", "D")]
    graph = build_directed_graph(edges)
    print(graph)
    print(neighbors(graph, "A"))
    print("Ожидается: build_directed_graph = {'A': ['B', 'C'], 'B': ['D'], 'C': [], 'D': []}, neighbors('A') = ['B', 'C']")
    print("Реализуй базовые функции представления графа.")
