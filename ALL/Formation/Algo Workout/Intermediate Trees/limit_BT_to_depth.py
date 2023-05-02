'''
Q:
Prompt

Given a binary tree and a depth, remove all nodes that are lower than that depth.
Examples

Input:
tree:
          1 
        /    \
      2       3
     / \      / 
   5   4   6 
     \
      7
k (depth): 1
Output: 
          1 
        /    \
      2       3
'''
class TreeNode(object):
    def __init__(self,value=0,left=None,right=None):
        self.value = value 
        self.left = left
        self.right = right 
        
def limitToKLevelsBT(root:TreeNode, depth:int)->TreeNode:
    if not root:
        return root
    
    if depth == 0:
        root.left = None
        root.right = None 
        return root 
    
    root.left = limitToKLevelsBT(root.left,depth-1)
    root.right = limitToKLevelsBT(root.right,depth-1) 
    return root 

Tree = TreeNode(1, TreeNode(2,TreeNode(5,None,TreeNode(7)),TreeNode(4)),TreeNode(3,TreeNode(6)))
new_tree = limitToKLevelsBT(Tree,1)
print(new_tree.value)
print(new_tree.left.value)
print(new_tree.right.value)
