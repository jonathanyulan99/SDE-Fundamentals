'''
Given the root of a binary tree, invert the tree, and return its root.
'''
class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val = val 
        self.left = left 
        self.right = right 

def invert_tree(root:TreeNode)->TreeNode:
    if not root:
        return root 
    # return TreeNode(root.val,invert_tree(root.right),invert_tree(root.left) if root else None  
    root.left, root.right = root.right,root.left 
    invert_tree(root.left)
    invert_tree(root.right)
    
    return root 
