'''
Q:
Prompt

Given a binary tree, give all nodes with one child an additional child with the value zero. 
If the node has two children or is a leaf node, do nothing.
Examples

Input4:
          1 
        /    \
      2       3
     /           \
   4              6
      \
        7
Output4:
          1 
        /    \
      2       3
     /  \     /  \
   4    0  0    6
  /  \
0     7
'''
class TreeNode(object):
    def __init__(self,value=0,left=None,right=None):
        self.value = value 
        self.left = left 
        self.right = right 
        
def fillZeroNodes(root:TreeNode)->TreeNode:
    if not root:
        return None 
    
    root.left = fillZeroNodes(root.left) 
    root.right = fillZeroNodes(root.right)
    
    if root.left and not root.right:
        root.right = TreeNode(0)
    
    elif root.right and not root.left: 
        root.left = TreeNode(0)
        
    return root 

Tree = TreeNode(1,TreeNode(2,TreeNode(4,None,TreeNode(7))),TreeNode(3,None,TreeNode(6)))
fillZeroNodes(Tree)