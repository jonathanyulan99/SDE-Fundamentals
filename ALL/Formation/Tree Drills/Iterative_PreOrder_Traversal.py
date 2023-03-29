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

'''


class TreeNode(object):
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# preOrder node, left, right
# normally handled with DFS/Recrusion


def pre_order_traversal(head: TreeNode) -> list:
    stack = [head]
    result = []

    while stack:
        node = stack.pop()
        result.append(node.value)
        print(node.value, end=' ')

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    print()
    return result


'''
        6
    4
        5
2       
    1
        0
'''
tree = TreeNode(2, TreeNode(1, TreeNode(0), TreeNode(1.5)),
                TreeNode(4, TreeNode(5, TreeNode(6))))

print(pre_order_traversal(tree))


def rec_pre_order_traversal(head: TreeNode) -> list:
    def dfs(root):
        if not root:
            return

        result.append(root.value)
        dfs(root.left)
        dfs(root.right)

    result = []
    dfs(head)
    return result


print(rec_pre_order_traversal(tree))
