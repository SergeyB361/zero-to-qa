def build_directed_graph(edges: list[tuple[str, str]]) -> dict[str, list[str]]:
    graph: dict[str, list[str]] = {}
    for left, right in edges:
        graph.setdefault(left, []).append(right)
        graph.setdefault(right, [])
    return graph



def build_undirected_graph(edges: list[tuple[str, str]]) -> dict[str, list[str]]:
    graph: dict[str, list[str]] = {}
    for left, right in edges:
        graph.setdefault(left, []).append(right)
        graph.setdefault(right, []).append(left)
    return graph


if __name__ == "__main__":
    edges = [("A", "B"), ("A", "C"), ("B", "D")]
    print(build_directed_graph(edges))
    print(build_undirected_graph(edges))
