
'''
❓ PROMPT
Given a binary tree and two nodes in the tree, find the lowest common ancestor of the two nodes. 
The lowest common ancestor of two nodes is the last node where both nodes share the same parent.

Example(s)
     1 <--- root
  2      3
4   5  6   7

lowestCommonAncestor(root, node4, node5) == node2
lowestCommonAncestor(root, node2, node3) == root
lowestCommonAncestor(root, root, node7) == root
lowestCommonAncestor(root, node5, node6) == root
lowestCommonAncestor(root, node3, node3) == node3  (self)
 

🔎 EXPLORE
List your assumptions & discoveries:
 

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
function lowestCommonAncestor(root, target1, target2) {
def lowestCommonAncestor(root: Node, target1: Node, target2: Node) -> Node:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
class Node(object):
    def __init__(self,val,left=None,right=None):
        self.val = val 
        self.left = left
        self.right = right 
        
def lowestCommonAncestor(root: Node, target1: Node, target2: Node) -> Node:
    if not root:
        return root
    
    if root == target1 or root == target2:
        return root 
    
    if target1 == target2:
        return target1
    
    left = lowestCommonAncestor(root.left,target1,target2) 
    right = lowestCommonAncestor(root.right,target1,target2) 
    
    if left and right: return root 
    elif root is not left and left:
        return left 
    elif root is not right and right:
        return right 
    elif left and not right: return left 
    else: return right 
    

oneNode = Node(1)
print(lowestCommonAncestor(oneNode, oneNode, oneNode) == oneNode)

#       1
#    2      3
#  4   5  6   7
node1 = Node(1)
node2,node3 = Node(2),Node(3)
node4,node5,node6,node7 = Node(4),Node(5),Node(6),Node(7)
node1.left,node1.right = node2,node3
node2.left,node2.right = node4,node5
node3.left,node3.right = node6,node7

print(lowestCommonAncestor(node1, node4, node6) == node1)
print(lowestCommonAncestor(node1, node2, node3) == node1)
print(lowestCommonAncestor(node1, node1, node7) == node1)
print(lowestCommonAncestor(node1, node5, node6) == node1)
print(lowestCommonAncestor(node1, node3, node3) == node3)

#           30
#     20         40
#  10   25     33   60
#   15 23    32       80
node30 = Node(30)
node20,node40 = Node(20),Node(40)
node10,node25,node33,node60 = Node(10),Node(25),Node(33),Node(60)
node15,node23,node32,node80 = Node(15),Node(23),Node(32),Node(80)
node30.left,node30.right = node20,node40
node20.left,node20.right = node10,node25
node40.left,node40.right = node33,node60
node10.right = node15
node25.left = node23
node33.left = node32
node60.right = node80

print(lowestCommonAncestor(node30, node15, node10) == node10)
print(lowestCommonAncestor(node30, node15, node23) == node20)
print(lowestCommonAncestor(node30, node15, node80) == node30)
print(lowestCommonAncestor(node30, node30, node30) == node30)
print(lowestCommonAncestor(node30, node32, node80) == node40)
print(lowestCommonAncestor(node30, node40, node60) == node40)