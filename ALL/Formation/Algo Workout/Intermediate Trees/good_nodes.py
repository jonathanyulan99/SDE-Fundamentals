'''
Given a binary tree root, a node X in the tree is named good if in the path from root to X,
there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
'''
class TNode(object):
    def __init__(self,val,left=None,right=None):
        self.val = val 
        self.left = left 
        self.right = right 
        
def good_nodes(root:TNode)->int:
    def dfs(root,_max):
        if not root:
            return 0 
        
        result = 0
        
        if root.val >= _max:
            result += 1 
            _max = root.val  
            
        result += dfs(root.left,_max) + dfs(root.right,_max) 
        return result 
        
    return dfs(root,root.val)    

root = [3,1,4,3,None,1,5]

tree = TNode(3,TNode(1
                     ,TNode(3)),TNode(4
                                      ,TNode(1),TNode(5)))

'''
            3
        1       4
    3          1  5   

Good Nodes: 4 
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
'''

from collections import deque
def level_order(root:TNode)->None:
    q = deque([root])
    
    while q:
        for _ in range(len(q)): 
            root = q.popleft() 
            print(root.val,end=' ') 
            if root.left: q.append(root.left)
            if root.right: q.append(root.right)
        print()

level_order(tree)
print(good_nodes(tree))