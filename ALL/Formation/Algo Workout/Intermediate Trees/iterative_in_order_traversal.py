'''
Practice Strength Algo: Iterative Inorder Traversal
'''
class TreeNode(object):
    def __init__(self,value=0,left=None,right=None):
        self.value = value 
        self.left = left 
        self.right = right 
        
def in_order_traversal_itr(root:TreeNode)->list[str]:
    if root:
        stack = [] 
        result = [] 
        
        while True: 
            while root:
                stack.append(root)  
                root = root.left 
            if not stack:
                return result 
            root = stack.pop() 
            result.append(root.value) 
            root = root.right
    return [] 

Tree = TreeNode(10,TreeNode(11,TreeNode(2),TreeNode(-1)),TreeNode(16,TreeNode(12,TreeNode(9),TreeNode(11))))
print(in_order_traversal_itr(Tree))