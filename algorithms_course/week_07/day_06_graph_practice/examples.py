from collections import deque


def node_count(graph: dict[str, list[str]]) -> int:
    return len(graph)



def edge_count_directed(graph: dict[str, list[str]]) -> int:
    total = 0
    for neighbors in graph.values():
        total += len(neighbors)
    return total



def shortest_reach(graph: dict[str, list[str]], start: str) -> dict[str, int]:
    queue = deque([start])
    dist = {start: 0}

    while queue:
        node = queue.popleft()
        for neighbor in graph.get(node, []):
            if neighbor not in dist:
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)
    return dist


if __name__ == "__main__":
    graph = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
    print(node_count(graph))
    print(edge_count_directed(graph))
    print(shortest_reach(graph, "A"))
