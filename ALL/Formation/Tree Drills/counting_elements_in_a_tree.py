class TNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


'''
Counts the total amout of nodes in a tree
Approach: 
    Use DFS with a stack 
    Need a result output instanitated to zero(0)
    If we have no root then its zero amount of nodes in the tree
    Stack appends the root
    Checks to see while we have an item in the stack
    stack.pop() and use that to check to increment our result += 1
    check for left and right children 
    stack.append(left)
    stack.append(right) 
'''


def count_elements_iteratively(root: TNode) -> int:
    if not root:
        return 0
    result = 0
    stack = []
    stack.append(root)

    while stack:
        root = stack.pop()
        if root.left:
            stack.append(root.left)
        if root.right:
            stack.append(root.right)
        result += 1

    return result


tree = TNode(1, TNode(3, TNode(2), TNode(4)), TNode(5, TNode(4), TNode(6)))
print(count_elements_iteratively(tree))


def count_elements_recursively(root: TNode) -> int:
    if not root:
        return 0

    return count_elements_recursively(root.left) + count_elements_recursively(root.right) + 1


print(count_elements_recursively(tree))
