class TNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def in_order_traversal(root: TNode) -> list:
    # set a current pointer to our root node
    current = root
    # need a stack to pop our left values from once we get to the
    # leaf node of our left-sub-tree
    stack = []
    # output to return is a list of node.values
    output = []

    # iterate through as long as we have a valid current/root
    while True:

        # check to see if we have a current value
        if current:
            # append our current to our stack to revisit once we have
            # explored our left-sub-tree fully
            stack.append(current)

            # explore our left-subtree, if we return None then we can explore
            # our stack values
            current = current. left

        # this condition will only execute once our current value is null which means
        # that our last appended TNode/current was our most left-sub-tree leaf
        elif stack:
            # reset our current pointer so that we can continue on in the next iteration of our
            # while loop
            current = stack.pop()
            output.append(current.value)
            print(current.value, end=' - ')

            # now since we are back at our most left-sub-tree leaf in the case of an intermediate node
            # we need to check the right child here which means we need to append back to our stack
            # the right sub-child
            current = current.right

        # if we have no more nodes on our stack and we have appended all of our values and our current pointer
        # has been reset to null than let us break out of our while loop
        else:
            break
    print("Done")

    return output


tree = TNode("A", TNode('B', TNode('C'), TNode('D')),
             TNode('E', None, TNode('F')))

tree_output = in_order_traversal(tree)
print(*tree_output)
