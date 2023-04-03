class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def tree_height_rec(root: TreeNode) -> int:
    # Write your code here.
    if not root:
        return -1

    left_subtree = tree_height_rec(root.left)
    right_subtree = tree_height_rec(root.right)
    return max(left_subtree, right_subtree) + 1


'''
                4
        2              6    
    1       3      5        7


'''

# Test Cases
print(tree_height_rec(None), -1)  # -1
print(tree_height_rec(TreeNode(1, TreeNode(2), TreeNode(3))), 1)  # 1
print(tree_height_rec(TreeNode(2, TreeNode(29, TreeNode(26)),
      TreeNode(4, None, TreeNode(2, TreeNode(9))))), 3)  # 3
print(tree_height_rec(TreeNode()), 0)  # 0
