class TNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Lets Implement DFS without the use of recursion
# Let us use a stack data structure LIFO
# Stack easily implemented with a list
# list.append(end of the stack)
# list.pop(defaults to -1 or last element in our list)
# LIFO because we want to visit the last node that was inputted in the stack


def dfs_with_pre_order_stack(root: TNode) -> list:
    if not root:
        return []

    result = []
    stack = []
    curr = root

    while curr or stack:
        if curr:
            result.append(curr.value)
            stack.append(curr)
            curr = curr.left
        elif not curr:
            curr = stack.pop()
            curr = curr.right
        else:
            break

    return result


tree = TNode(4, TNode(2, TNode(1), TNode(3)), TNode(6, TNode(5), TNode(7)))
print(dfs_with_pre_order_stack(tree))

# in order-means that the node is seen in order after we get to our most left subtree
# leftsubtree, node, rightsubtree


def dfs_with_in_order_stack(root: TNode) -> list:
    if not root:
        return []
    result = []
    stack = []
    curr = root

    while curr or stack:
        if curr:
            stack.append(curr)
            curr = curr.left
        elif not curr:
            curr = stack.pop()
            result.append(curr.value)
            curr = curr.right
        else:
            break

    return result


print(dfs_with_in_order_stack(tree))

# post_order means that our root value is seen last


def peek(stack):
    if len(stack) > 0:
        return stack[-1]
    return None


def dfs_with_post_order_stack(root: TNode) -> list:
    if not root:
        return []

    stack = []
    result = []
    curr = root

    while curr or stack:
        while curr:
            if curr.right:
                stack.append(curr.right)
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        if curr.right and len(stack) > 0 and stack[-1] == curr.right:
            stack.pop()
            stack.append(curr)
            curr = curr.right
        else:
            result.append(curr.value)
            curr = None
        if len(stack) == 0:
            break

    return result


print(dfs_with_post_order_stack(tree))
