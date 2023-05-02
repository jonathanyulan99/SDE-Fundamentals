'''
Q: Prompt 
Given a binary tree, return the count of non-leaf nodes.
Examples

Input:
          1 
        /    \
      2       3
     /        /
   4       5
Output: 3 (only 4 and 5 are leaf nodes)
'''

class TreeNode(object):
    def __init__(self,value=0,left=None,right=None):
        self.value = value 
        self.left = left 
        self.right = right 
        
def numberOfNonLeafNodes(root:TreeNode)->int:
    if not root or (not root.left and not root.right):
        return 0 
    
    return 1 + numberOfNonLeafNodes(root.left) + numberOfNonLeafNodes(root.right)
    
Tree = TreeNode(1,TreeNode(2,TreeNode(4,TreeNode(3.5),TreeNode(4.5))),TreeNode(3,TreeNode(5)))

print(numberOfNonLeafNodes(Tree))