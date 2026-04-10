# Неделя 8, День 4 - Повтор: search, trees, graphs
#
# Задание 1:
# Реализуй binary_search(items, target).
#
# Задание 2:
# Реализуй bfs_levels(graph, start).
#
# Задание 3:
# Реализуй preorder(root) для бинарного дерева.


from collections import deque


class TreeNode:
    def __init__(self, value: int, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right



def binary_search(items: list[int], target: int) -> int:
    return -1



def bfs_levels(graph: dict[str, list[str]], start: str) -> dict[str, int]:
    return {}



def preorder(root: TreeNode | None) -> list[int]:
    return []


if __name__ == "__main__":
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    graph = {"A": ["B", "C"], "B": ["D"], "C": [], "D": []}
    print(binary_search([1, 3, 5, 7], 5))
    print(bfs_levels(graph, "A"))
    print(preorder(root))
    print("Реализуй mixed practice по search, trees и graphs.")
