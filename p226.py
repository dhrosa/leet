class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root: TreeNode | None) -> TreeNode | None:
    if root is None:
        return None
    return TreeNode(root.val, invert_tree(root.right), invert_tree(root.left))
