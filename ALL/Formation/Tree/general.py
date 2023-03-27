class BinaryTreeNode(object):
    # can also be expanded to ternary trees by adding middle=none
    # can also be expanded to any n-tree by adding that many sub-tree/children references

    #      -                    -
    #   -     -            -    -    -
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TernaryTreeNode(object):
    def __init__(self, val, left=None, middle=None, right=None):
        self.val = val
        self.left = left
        self.middle = middle
        self.right = right


class QuadTreeNode(object):
    def __init__(self, val, topLeft=None, topRight=None, botLeft=None, botRight=None):
        self.val = val
        self.topLeft = topLeft
        self.topRight = topRight
        self.botLeft = botLeft
        self.botRight = botRight


def print_binary_tree(root: BinaryTreeNode):
    if root:
        print(root.value)
        print_binary_tree(root.left)
        print_binary_tree(root.right)


def print_ternary_tree(root: TernaryTreeNode):
    if root:
        print(root.val)
        print_ternary_tree(root.left)
        print_ternary_tree(root.middle)
        print_ternary_tree(root.right)


def print_quad_tree(root: QuadTreeNode):
    if root:
        print(root.val)
        print_quad_tree(root.topLeft)
        print_quad_tree(root.topRight)
        print_quad_tree(root.botLeft)
        print_quad_tree(root.botRight)


# binary tree
#    10
# 5     15
binary_root = BinaryTreeNode(10, BinaryTreeNode(5), BinaryTreeNode(15))
print_binary_tree(binary_root)
print()

#    10
# 5  11  15
ternary_root = TernaryTreeNode(10, TernaryTreeNode(
    5), TernaryTreeNode(11), TernaryTreeNode(15))
print_ternary_tree(ternary_root)
print()

#    10
#  5    11
# 15    20
quad_root = QuadTreeNode(10, QuadTreeNode(5), QuadTreeNode(
    11), QuadTreeNode(15), QuadTreeNode(20))
print_quad_tree(quad_root)
print()
