class TNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def get_height(node: TNode):
    # this is negative one because this would terminate on the case of a tree node that is None
    # if None is passed then we are at the children nodes of a leaf node which has none
    # return -1
    # thus once we get to a leaf node we see the case
    # max(-1,-1) which is -1 + 1 = 0
    # height of a leaf node is 0
    if not node:
        return -1

    return max(get_height(node.left), get_height(node.right))+1


tree = TNode(1, TNode(2, TNode(4), TNode(5, TNode(4.5), TNode(6))),
             TNode(3, TNode(None), TNode(7)))
'''
                    1               depth:0 height:2
                2       3           depth:1 height:1 
            4      5                depth:2 height:0
                                    depth:X height:-1
'''
print(get_height(tree))


# Getting the depth is the largest amount of edges from a node to the root
# In this case we will count backwards, as the depth of a root node is zero
# so instead our leaf nodes will not get a -1 passed back once we get to our leaf nodes
# we will pass back a zero and count largest amount of edges to the root
# Height: The total amount of edges from a node to the deepest descendant/node in a tree
def get_depth(node: TNode):
    if not node:
        return 0

    left_subtree = get_depth(node.left)
    rigth_subtree = get_depth(node.right)

    return max(left_subtree, rigth_subtree)+1


print(get_depth(tree))
