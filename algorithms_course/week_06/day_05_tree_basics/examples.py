class TreeNode:
    def __init__(self, value: int, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.value = value
        self.left = left
        self.right = right



def tree_sum(root: TreeNode | None) -> int:
    if root is None:
        return 0
    return root.value + tree_sum(root.left) + tree_sum(root.right)



def tree_height(root: TreeNode | None) -> int:
    if root is None:
        return 0
    return 1 + max(tree_height(root.left), tree_height(root.right))


if __name__ == "__main__":
    root = TreeNode(10, TreeNode(5), TreeNode(20, TreeNode(15), TreeNode(30)))
    print(tree_sum(root))
    print(tree_height(root))
