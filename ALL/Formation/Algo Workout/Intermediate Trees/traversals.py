'''
BFS:
    If the solution close to the root
    If we want to expand our search gradually
    If there's a dense number of neighbors and connections
    If we are interested in organizing the search by level

DFS:
    If the solution is far from the root
    If there's a sparse number of neighbors
    If there are too many broad possibilities but the answer is deeply nested
    If we want to go deep down a path
    If we need to backtrack to calculate local results at each node
    If we are interested in organizing the search by subtree
'''

class TNode(object):
    def __init__(self,value=0,left=None,right=None):
        self.value = value 
        self.left = left 
        self.right = right 

Tree = TNode(1,TNode(2,
                     TNode(3),TNode(4)),TNode(5))

'''
            1
        2      5
     3    4
'''

'''
This algorithm explores the root, followed by the left subtree, and finally, the right subtree.
An example use-case is to clone a tree since the algorithm must create the root before creating the subtrees.
'''
def pre_order_DFS(root:TNode,result=[])->list:
    if not root:
        return result
    
    result.append(root.value) 

    pre_order_DFS(root.left,result)
    pre_order_DFS(root.right,result) 
    
    return result 

print(pre_order_DFS(Tree))

'''
This algorithm explores the left subtree, followed by the root, and finally, the right subtree. 
In a BST, this algorithm would traverse the nodes in their natural ordering.
An example use-case is to flatten a BST into a sorted array.
'''
def in_order_DFS(root:TNode,result=[])->list:
    if not root:
        return result
    
    in_order_DFS(root.left,result)
    result.append(root.value) 
    in_order_DFS(root.right,result) 
    
    return result 

print(in_order_DFS(Tree))

'''
This algorithm explores the left subtree, followed by the right subtree, and finally, the root.
An example use-case for this traversal is to delete a tree since the algorithm must delete the children before the root node.
'''
def post_order_DFS(root:TNode,result=[])->list:
    if not root:
        return result 
    
    post_order_DFS(root.left)
    post_order_DFS(root.right)
    result.append(root.value)
    
    return result 

print(post_order_DFS(Tree))

from collections import deque
def level_order_BFS(root:TNode):
    result = [] 
    if not root:
        return result 
    
    q = deque([root])
    
    while q:
        _q_size = len(q)
        for i in range(_q_size):
            node = q.pop()
            result.append(node.value)
            
            if node.left:
                q.appendleft(node.left)
            if node.right:
                q.appendleft(node.right)
    
    return result 

print(level_order_BFS(Tree))
    