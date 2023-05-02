'''
515. Find Largest Value in Each Tree Row

Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).
'''

class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left 
        self.right = right 
        
'''
             5
         2      6
       1   3     9     

'''
Tree = TreeNode(5,TreeNode(2,TreeNode(1),TreeNode(12)),TreeNode(6,None,TreeNode(9)))
# DFS APPROACH HADRDER CONCEPTUALLY 
def find_largest_row_value_dfs(root:TreeNode)->list[int]: 
    if not root:
        return root
    result = []
    def dfs(root,level):
        if not root:
            return 
        if len(result) == level:
            result.append(root.val) 
        result[level] = max(result[level],root.val) 
        
        dfs(root.left,level+1)
        dfs(root.right,level+1)
    
    dfs(root,0) 
    return result 

print(find_largest_row_value_dfs(Tree))

import collections 
def find_largest_row_value_bfs(root:TreeNode)->list[int]:
    if not root:
        return root 
    
    q = collections.deque([root])
    result = [] 
    while q:
        _max = float('-inf')
        for _ in range(len(q)):
            node = q.popleft()
            _max = max(_max,node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right) 
        result.append(_max)
    
    return result 

print(find_largest_row_value_bfs(Tree))