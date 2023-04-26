'''
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. 
(i.e., from left to right, then right to left for the next level and alternate between).
'''
from typing import Optional, List
from collections import deque
class TreeNode(object):
    def __init__(self,value=0,left=None,right=None):
        self.value = value 
        self.left = left 
        self.right = right 
        
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        q = deque([root]) 
        zigZag = True
        while q:
            q_size = len(q)
            result_list = [] 
            for i in range(q_size):
                root = q.popleft() 
                result_list.append(root.val)
                if root.left: q.append(root.left)
                if root.right: q.append(root.right)
            result_list = reversed(result_list) if not zigZag else result_list 
            result.append(result_list)
            zigZag = not zigZag
        return result