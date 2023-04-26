class Tree(object):
    def __init__(self,value,left=None,right=None):
        self.value = value 
        self.left = left
        self.right = right 
'''
Q. Given a binary tree, return the values of the nodes when facing the tree from the right side (from top to bottom).
'''
from collections import deque
def solution(root):
    if not root:
        return root 
    
    q = deque([root])
    result = [] 
    while q: 
        for _ in range(len(q)): 
            root = q.popleft() 
            if _ == 0:
                result.append(root.value) 
            if root.right: q.append(root.right)
            if root.left: q.append(root.left) 
    
    return result 

'''
Q. Construct a zigzag tree from an array (alternating right and left child), starting with right.
'''
def solution(array):
    height = 0
    root = (Tree(array[0]))
    curr = root 
    
    for element in array[1:]:
        if height % 2 == 0: 
            curr.right = Tree(element)
            curr = curr.right 
        elif height % 2 == 1:
            curr.left = Tree(element)
            curr = curr.left 
        height+=1 
    
    return root

'''
Q. Construct a right child only tree from a given array.
'''
def solution(array):
    root = Tree(-1)
    curr = root 
    
    for element in array:
        curr.right=Tree(element)
        curr = curr.right
    
    return root.right 

'''
Q. Given a binary tree, count the number of non-leaf nodes (leaf nodes do not have any children).
'''
def solution(root):
    if not root:
        return 0 
    
    result = 0 
    def dfs(root,result):
        if not root:
            return result 
        
        if root.left or root.right:
            result += 1 
        
        result = dfs(root.left,result)
        result = dfs(root.right,result)
        
        return result 
    
    return dfs(root,result)

'''
Q. Given a binary tree and a target k, count the number of nodes that has a value less than k.
'''
def solution(root, target):
    result = 0
    
    def dfs(root,result):
        if not root:
            return result  
        
        if root.value < target:
            result += 1 
        
        result = dfs(root.left,result)
        result = dfs(root.right,result)
        return result 
    
    return dfs(root,result)

'''
Given a binary tree and a target k, return any values in the tree that is repeated exactly k times. 
If multiple values are repeated k times, return the smaller value. If there isn't any value repeated k times, return -1.
'''
def solution(root, k):
    d = {} 
    result = []
    def helper(root):
        if not root:
            return 
        nonlocal d 
        
        counter = d.get(root.value,0)+1
        d[root.value] = counter
    
        helper(root.left)
        helper(root.right) 
    helper(root)
    
    print(d)
    for key,v in d.items():
        if v == k:
            result.append(key)
    
    if len(result) == 0: 
        return -1 

    result.sort() 
    print(result)
    return result[0]