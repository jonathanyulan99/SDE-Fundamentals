'''
Q. Prompt:
Given a binary tree, count the number of nodes whose values are equal to a given target.

Examples

Input:
tree:
          1 
        /    \
      2       3
     / \        \
   3   2        2 
target: 2
Output: 3

Do Both Iteratively + Recursively 
'''
class TreeNode(object):
    def __init__(self,value=0,left=None,right=None):
        self.value = value 
        self.left = left 
        self.right = right 
        
def countNodesTargetBT(root:TreeNode, target:int)->int:
    if not root:
        return 0
    
    count = 0 
    
    if target == root.value:
        count+=1 
    
    count += countNodesTargetBT(root.left,target)
    count += countNodesTargetBT(root.right,target)
    
    return count 

def count_nodes_with_value(root, target):
    if root is None:
        return 0

    count = 0
    stack = [root]

    while stack:
        node = stack.pop()
        if node.val == target:
            count += 1
        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)

    return count

def count_nodes_with_value(root, target):
    if root is None:
        return 0

    count = 0
    stack = [root]

    while stack:
        node = stack.pop()
        if node is not None and node.val == target:
            count += 1
        if node is not None and node.left is not None:
            stack.append(node.left)
        if node is not None and node.right is not None:
            stack.append(node.right)

    return count

class Node(object):
    def __init__(self,value=0,left=None,right=None):
        self.val = value 
        self.left = left 
        self.right = right 
      
def count_nodes_with_target(root:Node,target:int)->int:
  if root is None:
      return 0 
  count = 0 
  stack = [root]

  while stack:
    node = stack.pop()
    if node and node.val == target:
      count+=1 
    if node and node.left:
      stack.append(node.left)
    if node and node.right:
      stack.append(node.right)
  
  return count 

Tree = Node(5,Node(3,Node(5),Node(3)),Node(3,Node(5),Node(3)))
print(count_nodes_with_target(Tree,5))