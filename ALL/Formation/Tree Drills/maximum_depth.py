def getMaxDepth(root):
    if not root:
        return 0

    leftDepth = getMaxDepth(root.left)
    rightDepth = getMaxDepth(root.right)

    return max(leftDepth, rightDepth) + 1


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


#       10
#   5       15
# 2   7  12    17
leftLeft, leftRight = Node(2), Node(7)
rightLeft, rightRight = Node(12), Node(17)
left = Node(5, leftLeft, leftRight)
right = Node(15, rightLeft, rightRight)
root = Node(10, left, right)
rightLeft.right = Node(13)


def print_pre_order(root: Node):
    if root:
        print(root.val)
        print_pre_order(root.left)
        print_pre_order(root.right)
    else:
        return []


def print_in_order(root: Node):
    result = []
    if not root:
        return result

    if root:
        print_in_order(root.left)
        # print(root.val)
        result.append(root.val)
        print_in_order(root.right)
    else:
        return result


def print_post_order(root: Node):
    if root:
        print_post_order(root.left)
        print_post_order(root.right)
        print(root.val)


print_pre_order(root)
print()
print(print_in_order(root))
print()
print_post_order(root)
print()


def print_descending_order(root: Node):
    if not root:
        return

    print_descending_order(root.right)
    print(root.val, end=' ')
    print_descending_order(root.left)


print_descending_order(root)
