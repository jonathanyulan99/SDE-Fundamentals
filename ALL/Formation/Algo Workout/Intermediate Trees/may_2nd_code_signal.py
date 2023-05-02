'''
Q. Given a binary search tree, return the value of the violating node. When there is a violation, return the lowest node. If there is no violating node, return -1.

The properties of a binary search tree are that:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
A violating node occurs when one of these properties is not met.

For example, in this tree:

      5
    /  \
  2    10
   \
    8
We have a violation between 5 and 8 because 8 is not less than 5. Because 8 is the lower node, return 8.
'''
def solution(root):
    if not root:
        return -1 
        
    def helper(root,_min,_max):
        if not root:
            return None 
        
        if root.value < _min or root.value > _max:
            return root.value
        
        return helper(root.left,_min,root.value) or helper(root.right,root.value,_max)
        
    
    if root:=helper(root,float('-inf'),float('inf')):
        return root 
    return -1 
'''
Q. Given a binary tree, count the number of leaf nodes.

Leaf node is a node that does not have any child nodes.
'''
def solution(root):
    if not root:
        return root 
    
    count = 0 
    
    def helper(node,count):
        if not node:
            return count 
        
        if not node.left and not node.right:
            count += 1 
        
        count = helper(node.left,count)
        count = helper(node.right,count)
        return count
    
    count = helper(root,count)   
    return count 
'''
Q. Given a binary tree, count the number of distinct elements in the tree.

     1
   9   5
  1     3
returns 4.

     6
   6   5
  1   6
returns 3.
'''
def solution(root):
    distinct = set()
    if not root:
        return root 
    
    distinct.add(root.value)
    
    def helper(node,distinct):
        if not node:
            return 
        
        distinct.add(node.value) 
        helper(node.left,distinct)
        helper(node.right,distinct)
    
    helper(root.left,distinct) 
    helper(root.right,distinct)
    return len(distinct)
'''
Q. Given a binary tree, return the the maximum sum of nodes from the root to any leaf.

For example, in this tree:
1
2 3
4 5 6 7

There are 4 leaves, and thus 4 paths from root to leaf:
1 -> 2 -> 4, 1 -> 2 -> 5, 1 -> 3 -> 6, 1 -> 3 -> 7

The one with the maximum sum is 1 -> 3 -> 7, so return 11.
'''
def solution(root):
    if not root:
        return root 
    
    def helper(node,cc_sum):
        if not node:
            return cc_sum 
        
        cc_sum = cc_sum + node.value 
        
        left = helper(node.left,cc_sum)
        right = helper(node.right,cc_sum) 
        
        return max(left,right)
    
    return max(helper(root.left,root.value),helper(root.right,root.value))

'''
Q. Given a binary tree, count the number of elements with negative values in the tree.

0 is a non-negative integer.
'''
def solution(root):
    count = 0 
    if not root:
        return count 
        
    if root.value < 0: 
        count += 1 
    
    return count + solution(root.left) + solution(root.right) 
'''
Q. Given a binary tree, count the number of elements with odd values in the tree.
'''
def solution(root):
    count = 0 
    if not root:
        return count 
    
    def helper(root,cc):
        if not root:
            return cc 
        
        if root.value % 2 == 1:
            cc += 1 
        
        cc = helper(root.left,cc)
        cc = helper(root.right,cc) 
        return cc
    
    count = helper(root,0)
    return count