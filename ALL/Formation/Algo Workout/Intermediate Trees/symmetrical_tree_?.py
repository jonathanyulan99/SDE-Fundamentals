'''
101: Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
'''
class TreeNode(object):
    def __init__(self,value,left=None,right=None):
        self.val = value 
        self.left = left 
        self.right = right 

def is_symmetrical(root:TreeNode)->bool:
    if not root:
        # special case 
        return True 
    
    def helper(left,right):
        if not left or not right:
            # just compare here 
            return left == right 
        if left.val != right.val:
            return False 
        return helper(left.left,right.right) and helper(left.right,right.left) 
    return helper(root.left,root.right) 

Tree = TreeNode(1,TreeNode(2,TreeNode(3),TreeNode(4)),TreeNode(2,TreeNode(4),TreeNode(3)))
print(is_symmetrical(Tree))

def is_symmetrical_itr(root: TreeNode)->bool:
    stack = [] 
    if root: stack.append((root.left,root.right))
    
    while stack:
        left, right = stack.pop() 
        
        if left and right: 
            if left.val!= right.val: return False 
            stack.append((left.left,right.right))
            stack.append((left.right,right.left)) 
        
        elif left or right:
            return False 
    return True 

Tree = TreeNode(1,TreeNode(2,TreeNode(None),TreeNode(4)),TreeNode(2,TreeNode(4),TreeNode(3)))
print(is_symmetrical(Tree))