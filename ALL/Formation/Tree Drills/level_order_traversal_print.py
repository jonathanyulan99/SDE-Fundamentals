import my_queue


class TNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Level-Order Traversal Best to use a Queue
# Because We want to explore what is sequentially next in our Queue
# Before exploring that current node's children
# We want to explore our previous node's children entirely before going deeper
#           1
#       3         6
#   2     4     5    7
# [1,3,6,2,4,5,7]


def level_order(root: TNode):
    if not root:
        return []
    curr = root
    q = my_queue.Queue()
    q.enqueue(curr)
    output = []

    while q.size() > 0:
        curr = q.dequeue()
        # we can also just append to the output here
        output.append(curr.value)
        if curr.left:
            q.enqueue(curr.left)
        if curr.right:
            q.enqueue(curr.right)

    return output


tree = TNode(1, TNode(3, TNode(2), TNode(4)), TNode(6, TNode(5), TNode(7)))
print(level_order(tree))


def reverse_level_order(root: TNode):
    if not root:
        return []
    curr = root
    q = my_queue.Queue()
    q.enqueue(curr)
    temp_container = []
    output = []

    while q.size() > 0:
        curr = q.dequeue()
        # we can also just append to the output here
        temp_container.append(curr.value)
        if curr.left:
            q.enqueue(curr.right)
        if curr.right:
            q.enqueue(curr.left)

    while temp_container:
        output.append(temp_container.pop())

    # reverse the output at the end
    # return reversed(output)
    # or output.reverse() and return
    return output


tree = TNode(1, TNode(3, TNode(2), TNode(4)), TNode(6, TNode(5), TNode(7)))
print(reverse_level_order(tree))
