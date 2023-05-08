'''
Q. Given a non-empty binary tree, find the maximum path sum.

Note:
• A path is any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example:
• Given a binary tree: 
           1
          / \    
         2   3
        /     
      -1   
// returns 6 (1 + 2 + 3)
'''
class TreeNode(object):
    def __init__(self,value=0,left=None,right=None):
        self.val = value 
        self.left = left 
        self.right = right 
        
def mps(root: TreeNode) -> int:
    # Write your code here.
    if not root:
        return root 
    
    result = float('-inf')
    
    def dfs(root): 
        if not root:
            return 0 
        
        nonlocal result 
        left = dfs(root.left)
        right = dfs(root.right) 
        
        result = max(result,root.val+left+right) 
        
        return max(root.val+max(left,right),0)
    dfs(root)
    return result 