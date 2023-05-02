'''
623. Add One Row to Tree

Given the root of a binary tree and two integers val and depth, add a row of nodes with value val at the given depth depth.

Note that the root node is at depth 1.

The adding rule is:

Given the integer depth, for each not null tree node cur at the depth depth - 1, 
create two tree nodes with value val as cur's left subtree root and right subtree root.
cur's original left subtree should be the left subtree of the new left subtree root.
cur's original right subtree should be the right subtree of the new right subtree root.
If depth == 1 that means there is no depth depth - 1 at all, 
then create a tree node with value val as the new root of the whole original tree, and the original tree is the new root's left subtree.
'''
class TreeNode(object):
    def __init__(self,value=0,left=None,right=None):
        self.value = value 
        self.left = left 
        self.right = right 

class Side(object):
    #key mapping pair 
    LEFT = 'left'
    RIGHT = 'right'
        
class Solution(object):
    def add_one_row_to_tree(self,root:TreeNode,val:int,depth:int,side=Side.LEFT)->TreeNode:
        if not root:
            return root 
        
        # special case 
        if root:
            if depth == 1: 
                tree_node = TreeNode(val)
                # x.y = v 
                # setattr(x,'y',v)
                setattr(tree_node,side,root)
                return tree_node 
                

        root.left = self.add_one_row_to_tree(root.left,val,depth-1) 
        root.right = self.add_one_row_to_tree(root.right,val,depth-1,Side.RIGHT)
        return root 
    
Root = TreeNode(10)
left = TreeNode(5)
right = TreeNode(15) 

setattr(Root,'left',left)
setattr(Root,'right',right)
print(Root.left.value)
print(Root.right.value) 