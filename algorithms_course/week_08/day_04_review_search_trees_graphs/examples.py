from collections import deque


def binary_search(items: list[int], target: int) -> int:
    left = 0
    right = len(items) - 1
    while left <= right:
        mid = (left + right) // 2
        if items[mid] == target:
            return mid
        if items[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1



def bfs_order(graph: dict[str, list[str]], start: str) -> list[str]:
    visited = {start}
    queue = deque([start])
    result: list[str] = []
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return result


if __name__ == "__main__":
    print(binary_search([1, 3, 5, 7, 9], 7))
    print(bfs_order({"A": ["B", "C"], "B": ["D"], "C": [], "D": []}, "A"))
