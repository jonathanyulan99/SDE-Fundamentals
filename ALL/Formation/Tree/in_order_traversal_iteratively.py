class TreeNode(object):
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def in_order(root: TreeNode) -> None:
    stack = list()

    while True:

        if root:
            stack.append(root)
            root = root.left

        elif stack:
            node = stack.pop()
            print(node.value, end=' ')

            root = node.right

        else:
            break
    print()


def in_order_2(root: TreeNode) -> None:
    result, stack = [], []

    while True:
        while root:
            stack.append(root)
            root = root.left
        if not stack:
            return result
        node = stack.pop()
        result.append(node.value)
        root = node.right


tree_root = TreeNode(1)
tree_root.left = TreeNode(2)
tree_root.right = TreeNode(3)
tree_root.left.left = TreeNode(4)
tree_root.left.right = TreeNode(5)
tree_root.right.right = TreeNode(20)

print(in_order(tree_root))
