'''
🔎 EXPLORE
What are some other insightful & revealing test cases?
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
Write your algorithm.
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.
▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
✏️ Description
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
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
class TreeNode:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
        
def count_tree(root: TreeNode) -> int:
    # Write your code here.
    pass

# Test Cases
print(count_tree(None), 0)
print(count_tree(TreeNode(1, TreeNode(2), TreeNode(3))), 3)
print(count_tree(TreeNode(2, TreeNode(29, TreeNode(26)), TreeNode(4, None, TreeNode(2, TreeNode(9))))), 6)
print(count_tree(TreeNode()), 1)

'''


class TreeNode(object):
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def count_tree(root: TreeNode) -> int:
    _sum = 0
    if not root:
        return _sum

    stack = list()

    stack.append(root)

    while stack:
        _sum += 1
        node = stack.pop()

        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return _sum


print(count_tree(None), 0)
print(count_tree(TreeNode(1, TreeNode(2), TreeNode(3))), 3)
print(count_tree(TreeNode(2, TreeNode(29, TreeNode(26)),
      TreeNode(4, None, TreeNode(2, TreeNode(9))))), 6)
print(count_tree(TreeNode()), 1)
