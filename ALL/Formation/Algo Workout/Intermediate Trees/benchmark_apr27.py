'''
Given a binary tree of integers, return all the paths from the tree's root to its leaves as an array of strings. 
The strings should have the following format:
"root->node1->node2->...->noden", representing the path from root to noden, 
where root is the value stored in the root and node1,node2,...,noden are the values stored in the 1st, 2nd,..., and nth nodes 
in the path respectively (noden representing the leaf).
'''
class Node(object):
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left 
        self.right = right 
        
def paths_list(root:Node)->list[str]:
    result = []
    def paths(root,path,result):
        path += str(root.val)
        if not root.left and not root.right: 
            result.append(path)
        if root.left: 
            paths(root.left,path + '->',result)
        if root.right:
            paths(root.right,path+'->',result) 
    if root:
        paths(root,'',result)
    return result 

'''
                  5
            2          7
          1   3      6   8
'''
tree = Node(5,Node(2,Node(1),Node(3)),Node(7,Node(6),Node(8)))
print(paths_list(tree))

'''
Note: Your solution should have only one BST traversal and not use extra space beyond the recursive call stack.

A tree is considered a binary search tree (BST) if for each of its nodes the following is true:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and the right subtrees must also be binary search trees.
Given a binary search tree t, find the kth smallest element in it.

Note that kth smallest element means kth element in increasing order. See examples for better understanding.
'''
def kth_smallest(root:Node,k:int)->int:
    stack = [] 
    point = 0 
    
    curr = root 
    
    while True:
        if curr:
            stack.append(curr)
            curr = curr.left 
        elif stack:
            curr = stack.pop()
            point += 1 
            if point == k: 
                return curr
            curr = curr.right
        else:
            break
    
    return -1 

tree1 = Node(5,Node(2,Node(1),Node(3)),Node(7,Node(6),Node(8)))
print(kth_smallest(tree1,5).val)
             
    