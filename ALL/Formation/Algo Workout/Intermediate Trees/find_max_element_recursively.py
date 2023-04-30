class TreeNode(object):
    def __init__(self,value,left=None,right=None):
        self.value = value 
        self.left = left 
        self.right = right 
        
'''
            5
        3       7
      1   2    6  8 
'''

Tree = TreeNode(5,TreeNode(3,TreeNode(1),TreeNode(2)),TreeNode(7,TreeNode(6),TreeNode(8)))
        
def find_max_node(root:TreeNode)->TreeNode:
    def helper(curr,_max):
        if not curr:
            return _max 
        if curr.value > _max.value:
            _max = curr 
        _max = helper(curr.left,_max)
        _max = helper(curr.right,_max)
        return _max 
    if root:
        return helper(root,root)
    return None 

print(find_max_node(Tree).value)

def find_max_curr_val(root:TreeNode)->int:
    def helper(root,_max=float('-inf')):
        if not root:
            return _max 
        if root.value >= _max:
            _max = root.value 
        return max(root.value,helper(root.left,_max),helper(root.right,_max))
    if root:
        return helper(root)
    return None 

print(find_max_curr_val(Tree))