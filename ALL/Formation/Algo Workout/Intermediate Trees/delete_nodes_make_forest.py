'''
Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest. You may return the result in any order.
'''
class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val = val 
        self.left = left 
        self.right = right 
        
def make_forest(root:TreeNode,to_delete:list[int])->list[TreeNode]:
    to_delete = set(to_delete) 
    result = list() 
    def helper(root):
        if not root:
            return 
        
        root.left = helper(root.left)
        root.right = helper(root.right) 
        
        if root.val in to_delete:
            if root.left: result.append(root.left)
            if root.right: result.append(root.right) 
            return None 
        return root         
    if root:= helper(root):
        result.append(root)
    return result 

'''
        5
    2       7
  1   3   8   9
'''
Tree = TreeNode(5,TreeNode(2,TreeNode(1),TreeNode(3)),TreeNode(7,TreeNode(8),TreeNode(9)))

print(make_forest(Tree,[3,7]))