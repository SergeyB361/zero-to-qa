# Неделя 6, День 6 - DFS по дереву
#
# Задание 1:
# Реализуй preorder(root).
#
# Задание 2:
# Реализуй inorder(root).
#
# Задание 3:
# Реализуй postorder(root).


class TreeNode:
    def __init__(self, value: int, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right



def preorder(root: TreeNode | None) -> list[int]:
    return []



def inorder(root: TreeNode | None) -> list[int]:
    return []



def postorder(root: TreeNode | None) -> list[int]:
    return []


if __name__ == "__main__":
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    print(preorder(root))
    print(inorder(root))
    print(postorder(root))
    print("Реализуй DFS-обходы дерева.")
