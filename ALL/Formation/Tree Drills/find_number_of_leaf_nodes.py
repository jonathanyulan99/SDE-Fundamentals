class TNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


tree = TNode(1, TNode(2, TNode(4), TNode(5, TNode(8), TNode(9))),
             TNode(3, TNode(6), TNode(7)))

'''
                1 
        2               3
    4       5          6 7
           8 9
'''


def count_leaf_nodes(root: TNode) -> int:
    if not root:
        return 0

    if not root.left and not root.right:
        return 1

    left_leaves = count_leaf_nodes(root.left)
    right_leaves = count_leaf_nodes(root.right)

    return left_leaves + right_leaves


print(count_leaf_nodes(tree))

'''
count_leaf_nodes(root) 










'''
