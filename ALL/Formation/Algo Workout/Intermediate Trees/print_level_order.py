'''
Q. Given a binary tree, print level order traversal so that nodes of all levels are printed in several lines

Examples:
• Given a binary tree:
                 1
                / \ 
               2   3
// returns [[1], [2, 3]]

• Given a binary tree:
                 1
                / \
               2   3
              / \
             4   5

// returns [[1], [2, 3], [4, 5]]
'''
class TreeNode(object):
    def __init__(self,val,left=None,right=None):
        self.val = val 
        self.left = left
        self.right = right 
    
from collections import deque    
def printTree(root: TreeNode) -> list[int]:
    if not root:
        return [] 
    
    result = [] 
    q = deque([root])
    
    while q:
        level = [] 
        for _ in range(len(q)):
            node = q.popleft() 
            level.append(node.val) 
            if node.left: q.append(node.left)
            if node.right: q.append(node.right) 
        result.append(level) 
    
    return result 

Tree = TreeNode(1,TreeNode(2
                           ,TreeNode(4),TreeNode(5)),TreeNode(3))

print(printTree(Tree))

Tree = TreeNode(1,TreeNode(2),TreeNode(3))
print(printTree(Tree))

Tree = TreeNode(2, TreeNode(29, TreeNode(26)), TreeNode(4, None, TreeNode(2, TreeNode(9))))
print(printTree(Tree))
