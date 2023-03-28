import collections


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def find_bfs(root: TreeNode, target: int) -> bool:
    # Write your code here.
    if not root:
        return False

    queue = collections.deque([root])

    while queue:
        node = queue.pop()
        if node.value == target:
            return True
        if node.left:
            queue.appendleft(node.left)
        if node.right:
            queue.appendleft(node.right)

    return False


# Test Cases
tree1 = TreeNode(3, TreeNode(29, TreeNode(2)),
                 TreeNode(4, None, TreeNode(2, TreeNode(9))))
print(find_bfs(None, 1), False)
print(find_bfs(tree1, 9), True)
print(find_bfs(tree1, 1), False)
print(find_bfs(tree1, 2), True)
print(find_bfs(TreeNode(1), 2), False)
tester = (1, 2)
lst = list()
lst.append(tester)
print(lst[0][0], lst[0][1])
