class TreeNode:
    def __init__(self, value: int, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.value = value
        self.left = left
        self.right = right



def preorder(root: TreeNode | None) -> list[int]:
    if root is None:
        return []
    return [root.value] + preorder(root.left) + preorder(root.right)



def inorder(root: TreeNode | None) -> list[int]:
    if root is None:
        return []
    return inorder(root.left) + [root.value] + inorder(root.right)


if __name__ == "__main__":
    root = TreeNode(10, TreeNode(5), TreeNode(20, TreeNode(15), TreeNode(30)))
    print(preorder(root))
    print(inorder(root))
