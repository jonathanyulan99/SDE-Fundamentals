class TreeNode(object):
    def __init__(self,value=0,left=None,right=None):
        self.value = value 
        self.left = left 
        self.right = right 
        
def sum_tree(root:TreeNode)->int:
    if not root:
        return 0 
    
    return sum_tree(root.left) + sum_tree(root.right) + root.value

print(sum_tree(None), 0)
print(sum_tree(TreeNode(1, TreeNode(2), TreeNode(3))), 6)
print(sum_tree(TreeNode(1)), 1)
from collections import deque

def sum_tree_iterative(root:TreeNode)->int:
    _sum = 0 
    if not root:
        return _sum
    
    q = deque([root])
    
    while q:
        root = q.pop() 
        _sum += root.value 
        if root.left:
            q.appendleft(root.left)
        if root.right:
            q.appendleft(root.right)
    
    return _sum 

print(sum_tree_iterative(None), 0)
print(sum_tree_iterative(TreeNode(1, TreeNode(2), TreeNode(3))), 6)
print(sum_tree_iterative(TreeNode(1)), 1)

q = deque([1,2,3])
print(q.pop()) #pops from the right side 
print(q.popleft()) #pops from the left side 
q.appendleft(5) # 5->2
q.append(7)# 5<->2<->7

while q: 
    print(q.pop())