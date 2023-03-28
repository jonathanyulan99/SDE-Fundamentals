import collections


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root: TreeNode) -> list[int]:
    result = []

    if not root:
        return []

    queue = collections.deque([root])

    while queue:
        level_values = list()
        queue_size = len(queue)
        for i in range(queue_size):
            t_node = queue.pop()
            level_values.append(t_node.val)
            if t_node.left:
                queue.appendleft(t_node.left)
            if t_node.right:
                queue.appendleft(t_node.right)
        result.append(level_values)

    return result


print(level_order(root=TreeNode(2, TreeNode(29, TreeNode(26)),
      TreeNode(4, None, TreeNode(2, TreeNode(9))))))
