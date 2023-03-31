'''

Mar 30 

'''


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#     100
#   99   101
# 98


a = TreeNode(98)
left, right = TreeNode(99, a), TreeNode(101)
root = TreeNode(100, left, right)


root.left = None

#      10
#   5       15
# 1   7   12   20
#        11
#     10.5

#      10
#   5       15
# 1   7   11   20
#      10.5 12
#

#      10
#   5       15
# 1   7   12   20
#        11
#


def returnDepth(root):
    if not root:
        return -1

    return 1 + max(returnDepth(root.left), returnDepth(root.right))


def sumAllNodes(root: TreeNode):
    if not root:
        return 0

    return root.value + sumAllNodes(root.left) + sumAllNodes(root.right)


def search(root, target):
    if not root:
        return False

    if target == root.value:
        return True
    elif target < root.value:
        return search(root.left, target)
    else:
        return search(root.right, target)


def isValidBST(root: TreeNode, floor=float('-inf'), ceiling=float('inf')) -> bool:
    if not root:
        return True
    if root.val <= floor or root.val >= ceiling:
        return False

    # in the left branch, root is the new ceiling
    # in the right branch, root is the new floor
    return isValidBST(root.left, floor, root.val) \
        and isValidBST(root.right, root.val, ceiling)


print("Is this a valid BST? " + str(isValidBST(root) == True))

''''
        1
    2       3     
'''
