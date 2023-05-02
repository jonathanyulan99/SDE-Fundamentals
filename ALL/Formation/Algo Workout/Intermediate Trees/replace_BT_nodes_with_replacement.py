'''
Q. Prompt: 

Given a binary tree, a target and a replacement, replace all nodes whose values match the target value with the replacement value.
Examples

Input:
tree:
          1 
        /    \
      2       3
     / \         \
   3   4         2
target: 2,
replacement: 5

Output: 
          1 
        /    \
      5       3
     / \         \
   3   4         5
'''
class TreeNode(object):
    def __init__(self,value=0,left=None,right=None):
        self.value = value 
        self.left = left 
        self.right = right 
        
def replaceNodeValuesBT(root, target:int, replacement:int)->TreeNode:
    if not root:
        return None 
    
    if root.value == target:
        root.value = replacement
    
    replaceNodeValuesBT(root.left,target,replacement)
    replaceNodeValuesBT(root.right,target,replacement)
    
    return root 