# Неделя 1, День 7 - Мини-проект: Tree Explorer


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


def preorder(root: TreeNode | None) -> list[int]:
    return []


def main() -> None:
    root = TreeNode(4, TreeNode(2), TreeNode(7, TreeNode(6), None))

    print('Tree Explorer demo scaffold')
    print('tree_sum ->', tree_sum(root), '| expected: 19')
    print('tree_size ->', tree_size(root), '| expected: 4')
    print('tree_height ->', tree_height(root), '| expected: 3')
    print('preorder ->', preorder(root), '| expected: [4, 2, 7, 6]')


if __name__ == "__main__":
    main()
