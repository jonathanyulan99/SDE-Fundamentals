'''
❓ PROMPT
Given the root of a binary tree, return true if the given tree is immediately distinct, or false otherwise. 
A binary tree is immediately distinct if no parent node in the tree has a child node with the same value as itself.

For example, if the parent node = *1* and it has a child node of the same value *1*, this would not be an immediately 
distinct tree. On the other hand, if no nodes have a child node with the same value as themselves, this is an 
immediately distinct tree.

Example(s)
           1*
       1*      2
     3   4   _   6
should return false

           1
       2       2
    5    9   _   _    
should return true
 

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
function treeIsImmediatelyDistinct(root) {
def treeIsImmediatelyDistinct(root: Node) -> bool:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
class TreeNode(object):
    def __init__(self,value=0,left=None,right=None):
        self.val = value 
        self.left = left 
        self.right = right 
        
def treeIsImmediatelyDistinct(root: TreeNode) -> bool:
    if not root:
        return True 
    
    def dfs(root,_prev):
        if not root:
            return True 
        
        if root.val == _prev:
            return False 
        
        return dfs(root.left,root.val) and dfs(root.right,root.val) 
        
    return dfs(root,None)

#    1
#  1   2
# 3 4    6
root = TreeNode(1,
        TreeNode(1,
          TreeNode(3),
          TreeNode(4)
          ),
        TreeNode(2,
          None,
          TreeNode(6)
          )
        )
print(treeIsImmediatelyDistinct(root) is False)

#    1
#  2   2
# 5 9
root = TreeNode(1,
        TreeNode(2,
          TreeNode(5),
          TreeNode(9)
          ),
        TreeNode(2)
        )
print(treeIsImmediatelyDistinct(root) is True)

#  2
# 5 9
root = TreeNode(2,
        TreeNode(5),
        TreeNode(9))
print(treeIsImmediatelyDistinct(root) is True)

# 2
root = TreeNode(2)
print(treeIsImmediatelyDistinct(root) is True)

#  1
# 5 1
root = TreeNode(1,
        TreeNode(5),
        TreeNode(1))
print(treeIsImmediatelyDistinct(root) is False)

#  1
# 2 2
root = TreeNode(1,
        TreeNode(2),
        TreeNode(2))
print(treeIsImmediatelyDistinct(root) is True)

#    1
#  2
# 1
root = TreeNode(1,
        TreeNode(2,
          TreeNode(1)
          )
        )
print(treeIsImmediatelyDistinct(root) is True)

#    1
#  1
# 1 1
root = TreeNode(1,
        TreeNode(1,
          TreeNode(1),
          TreeNode(1)
          )
        )
print(treeIsImmediatelyDistinct(root) is False)

#    6
#  8
# 4 8
root = TreeNode(6,
        TreeNode(8,
          TreeNode(4),
          TreeNode(8)
          )
        )
print(treeIsImmediatelyDistinct(root) is False)

#    6
#   8
#  4
# 8
root = TreeNode(6,
        TreeNode(8,
          TreeNode(4,
            TreeNode(8)
            )
          )
        )
print(treeIsImmediatelyDistinct(root) is True)

#    6
#   8
#  4
# 6
root = TreeNode(6,
        TreeNode(8,
          TreeNode(4,
            TreeNode(6)
            )
          )
        )
print(treeIsImmediatelyDistinct(root) is True)