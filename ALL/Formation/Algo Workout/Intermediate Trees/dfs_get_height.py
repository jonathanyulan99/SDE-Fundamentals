class TNode(object):
    def __init__(self,val,left=None,right=None):
        self.val = val 
        self.left = left 
        self.right = right 

def get_height(root:TNode):
    if not root: 
        return -1 
    
    left = get_height(root.left) 
    right = get_height(root,right) 
    
    return max(left,right) + 1 