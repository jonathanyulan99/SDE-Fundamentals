class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: TreeNode) -> int:
    if not root:
        return 0

    left = max_depth(root.left)
    right = max_depth(root.right)

    return max(left, right) + 1


print(max_depth(root=TreeNode(2, TreeNode(29, TreeNode(26)),
      TreeNode(4, None, TreeNode(2, TreeNode(9))))))
