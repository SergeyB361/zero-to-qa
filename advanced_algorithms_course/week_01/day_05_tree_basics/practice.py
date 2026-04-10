# Неделя 1, День 5 - Деревья: база
#
# Задание 1:
# Реализуй tree_sum(root).
#
# Задание 2:
# Реализуй tree_size(root) -> количество узлов.
#
# Задание 3:
# Реализуй tree_height(root).
# Считай высоту в узлах: для пустого дерева 0, для дерева из одного узла 1.


class TreeNode:
    def __init__(self, value: int, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right



def tree_sum(root: TreeNode | None) -> int:
    return -1



def tree_size(root: TreeNode | None) -> int:
    return -1



def tree_height(root: TreeNode | None) -> int:
    return -1


if __name__ == "__main__":
    root = TreeNode(4, TreeNode(2), TreeNode(7, TreeNode(6), None))
    print(tree_sum(root))
    print(tree_size(root))
    print(tree_height(root))
    print("Ожидается: tree_sum = 19, tree_size = 4, tree_height = 3")
    print("Реализуй базовые функции для дерева.")
