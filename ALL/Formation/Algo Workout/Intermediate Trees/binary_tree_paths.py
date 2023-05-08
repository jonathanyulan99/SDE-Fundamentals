'''
257. Binary Tree Paths

Given the root of a binary tree, return all root-to-leaf paths in any order.
A leaf is a node with no children.
'''
class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left 
        self.right = right 
        

def binary_tree_paths_itr(root:TreeNode)->list[str]:
    if not root:
        return [] 
    
    result = []
    stack = [(root,'')]
    
    while stack:
        node,path = stack.pop() 
        if not node.left and not node.right: 
            # leaf node case 
            result.append(path+str(root.val))
        if node.left:
            stack.append((node.left,path+str(node.val)+'->'))
        if node.right:
            stack.append((node.right,path+str(node.val)+'->'))
    return result 

def binary_tree_paths_rec(root: TreeNode)->list[str]:
    if not root:
        return []
    
    result =[]
    def dfs_helper(root,path):
        if not root.left and not root.right: 
            result.append(path+str(root.val))
        
        if root.left: 
            dfs_helper(root.left,path+str(root.val)+'->')
        if root.right:
            dfs_helper(root.right,path+str(root.val)+'->')
    
    dfs_helper(root,'')
    return result 

root = TreeNode(1,
  TreeNode(2,
     TreeNode(9),
     TreeNode(8)
  ),
  TreeNode(2,
      TreeNode(4),
      TreeNode(1)
  )
)

print(binary_tree_paths_itr(root))
print(binary_tree_paths_rec(root))