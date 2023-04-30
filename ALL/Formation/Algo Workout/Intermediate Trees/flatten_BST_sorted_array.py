class TreeNode(object):
    def __init__(self,value,left=None,right=None):
        self.value = value 
        self.left = left 
        self.right = right 

def flatten_BST(root:TreeNode)->list[int]:
    result = []
    def helper(root):
        if not root:
            return 
        
        helper(root.left) 
        result.append(root.value)
        helper(root.right) 
    if root:=helper(root):
        return result 
    return result 

'''
          5     
      2       7      ==> [1,2,3,5,6,7,9]
    1   3   6   9
'''

Tree = TreeNode(5,TreeNode(2,TreeNode(1),TreeNode(3)),TreeNode(7,TreeNode(6),TreeNode(9)))

print(flatten_BST(Tree))