def dfs_order(graph: dict[str, list[str]], start: str) -> list[str]:
    result: list[str] = []
    visited: set[str] = set()

    def dfs(node: str) -> None:
        visited.add(node)
        result.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor)

    dfs(start)
    return result


if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["E"],
        "D": [],
        "E": [],
    }
    print(dfs_order(graph, "A"))
