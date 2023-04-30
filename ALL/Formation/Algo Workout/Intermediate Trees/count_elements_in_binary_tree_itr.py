'''
Q. Given a binary tree, count the number of elements in the tree.

Example:
• Given a binary tree:
                 1
                / \
               7   3
              / \
             4   5
// returns 5

▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
🟦 Python
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
'''

class TreeNode:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
import collections     
def count_tree(root: TreeNode) -> int:
    if not root:
        return 0 
    q = collections.deque([root])
    num_elements = 0 
    while q: 
        node = q.popleft() 
        num_elements += 1 
        if node.left: q.append(node.left) 
        if node.right: q.append(node.right)
    
    return num_elements

def count_tree(root:TreeNode)->int:
    num_elements = 0 
    def helper(root,num_elements):
        if not root: 
            return num_elements
        num_elements += 1 
        num_elements = helper(root.left,num_elements)
        num_elements = helper(root.right,num_elements)
        return num_elements
    if root:
        num_elements = helper(root,num_elements)
    return num_elements

def count_tree(root:TreeNode)->int:
    num_elements = 0 
    def helper(root):
        if not root: 
            return 0 
        left = helper(root.left)
        right = helper(root.right) 
        return 1 + left + right 
    if root:
        num_elements = helper(root)
    return num_elements

# Test Cases
print(count_tree(None), 0)
print(count_tree(TreeNode(1, TreeNode(2), TreeNode(3))), 3)
print(count_tree(TreeNode(2, TreeNode(29, TreeNode(26)), TreeNode(4, None, TreeNode(2, TreeNode(9))))), 6)
print(count_tree(TreeNode()), 1)

