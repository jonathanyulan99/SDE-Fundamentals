class TNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def get_number_of_objects(root: TNode) -> int:
    if not root:
        return 0

    def helper(root, count=1):
        if not root:
            return 0

        if root.left:
            count = helper(root.left, count+1)
        if root.right:
            count = helper(root.right, count+1)

        return count

    return helper(root)


tree = TNode(2, TNode(1, TNode(0)), TNode(3))
tree = TNode(1, TNode(2, TNode(4), TNode(5, TNode(8), TNode(9))),
             TNode(3, TNode(6), TNode(7)))


'''
                1 
        2               3
    4       5          6 7
           8 9
'''

print(get_number_of_objects(tree))

'''
f(root): ---> return 9 is our answer
helper(1,count=1): count = helper(2,count=2) return 6 + helper(3,count=7)---> returned 9 ---> return count(9) 
helper(2,count=2): count = helper(4,count=3) return 3 + helper(5,count=4) ---> return 6 --> return count to root 
helper(4,count=3): return count here no more to explore 
    helper(5,count=4): helper(8,count=5) return 5 + helper(9,count=6) return 6 ---> now we return count 
    helper(8,count=5): return count here 
        helper(9,count=6): return count because no left or right subtrees 
            helper(3,count=7): helper(6,count=8) return 8 + helper(7,count=9) --> returned 9 ---> return count to original caller
            helper(6,count=8): no left or right so return counter back
                helper(7,count=9): no left or right so return counter 
'''
