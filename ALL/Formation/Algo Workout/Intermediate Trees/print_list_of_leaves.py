class TNode(object):
    def __init__(self,val,left=None,right=None):
        self.val = val 
        self.left = left 
        self.right = right 


def print_leaves_order(root:TNode)->list[list[int]]:
    result = [] 
    def helper(root):
        if not root:
            return 0 
        
        nonlocal result 
        left = helper(root.left)
        right = helper(root.right) 
        
        height = max(left,right) + 1 

        if len(result) < height:
            result.append([])
        result[height-1].append(root.val) 
        return height 
    
    helper(root)
    return result 
    
'''
             3
        6        8
     2    11       13
         9  5     7

result = [[2,9,5,7],[11,13],[6,8],[3]]
'''
tree = TNode(3,TNode(6,
                     TNode(2),TNode(11,
                                    TNode(9),TNode(5))),TNode(8,
                              None, TNode(13
                                          ,TNode(7))))

print(print_leaves_order(tree))