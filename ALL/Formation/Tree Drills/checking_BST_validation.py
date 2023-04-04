class TNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_valid_bst(root: TNode) -> bool:
    def helper(root, _min=float('-inf'), _max=float('inf')):
        if not root:
            return True

        if root.value <= _min or root.value >= _max:
            return False

        return helper(root.left, _min, root.value) and helper(root.right, root.value, _max)

    return helper(root)


leftLeft, leftRight = TNode(2), TNode(7)
rightLeft, rightRight = TNode(12), TNode(17)
left = TNode(5, leftLeft, leftRight)
right = TNode(15, rightLeft, rightRight)
root = TNode(10, left, right)
rightLeft.right = TNode(13)

print(is_valid_bst(root))
