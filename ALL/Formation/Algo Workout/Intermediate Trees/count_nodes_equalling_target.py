'''
Q. Prompt:
Given a binary tree, count the number of nodes whose values are equal to a given target.

Examples

Input:
tree:
          1 
        /    \
      2       3
     / \        \
   3   2        2 
target: 2
Output: 3

Do Both Iteratively + Recursively 
'''
class TreeNode(object):
    def __init__(self,value=0,left=None,right=None):
        self.value = value 
        self.left = left 
        self.right = right 
        
def countNodesTargetBT(root:TreeNode, target:int)->int:
    if not root:
        return 0
    
    count = 0 
    
    if target == root.value:
        count+=1 
    
    count += countNodesTargetBT(root.left,target)
    count += countNodesTargetBT(root.right,target)
    
    return count 