'''
▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
✏️ Description
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
Q. Given a binary tree, determine if it is a valid binary search tree (BST).

Examples:
• Given a binary tree:
        2
       / \
      1   3
// returns True

• Given a binary tree:
        1
       / \
      2   3
// returns False

'''


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def validate_bst(root: TreeNode) -> bool:
    # Write your code here.
    '''if not root:
        return True

    if root.left and root.left.value >= root.value:
        return False
    if root.right and root.right.value <= root.value:
        return False

    return validate_bst(root.left) and validate_bst(root.right)'''

    def helper(root, _min, _max):
        if not root:
            return True

        if root.value <= _min or root.value >= _max:
            return False

        return helper(root.left, _min, root.value) and helper(root.right, root.value, _max)

    return helper(root, -float('inf'), float('inf'))


# Verify
tree1 = TreeNode(2, TreeNode(1), TreeNode(3))
tree2 = TreeNode(1, TreeNode(2), TreeNode(3))
tree3 = TreeNode(8, TreeNode(3, TreeNode(1), TreeNode(6)),
                 TreeNode(10, None, TreeNode(14, TreeNode(13))))
tree4 = TreeNode(8, TreeNode(3, TreeNode(1), TreeNode(9)),
                 TreeNode(10, None, TreeNode(14, TreeNode(13))))
print(validate_bst(None), True)
print(validate_bst(tree1), True)
print(validate_bst(tree2), False)
print(validate_bst(tree3), True)
print(validate_bst(tree4), False)

'''
                8
            3
        1     9

'''


def validate_bst_2(root: TreeNode) -> bool:
    return helper2(root, -float('inf'), float('inf'))


def helper2(root, _min, _max):
    if not root:
        return True

    if root.value < _min or root.value > _max:
        return False

    return helper2(root.left, _min, root.value) and helper2(root.right, root.value, _max)


print(validate_bst_2(None), True)
print(validate_bst_2(tree1), True)
print(validate_bst_2(tree2), False)
print(validate_bst_2(tree3), True)
print(validate_bst_2(tree4), False)
