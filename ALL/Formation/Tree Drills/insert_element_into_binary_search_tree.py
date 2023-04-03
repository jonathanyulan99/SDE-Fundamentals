class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def arrayifyTree(root: TreeNode):
    if root is None:
        return []
    queue = []
    array = []
    queue.append(root)
    while (len(queue) != 0):
        node = queue.pop(0)
        array.append(node.value)
        if (node.left):
            queue.append(node.left)
        if (node.right):
            queue.append(node.right)
    return array


def insert_bst(root: TreeNode, target: int) -> TreeNode:
    # Write your code here.
    if not root:
        return TreeNode(target)

    if target < root.value:
        left_child = insert_bst(root.left, target)
        root.left = left_child
        return root
    else:
        right_child = insert_bst(root.right, target)
        root.right = right_child
        return root


def insert_bst(root: TreeNode, target: int) -> TreeNode:
    if not root:
        return TreeNode(target)

    stack = [root]

    while stack:
        curr = stack.pop()
        if target < curr.value:
            if curr.left:
                stack.append(curr.left)
            else:
                curr.left = TreeNode(target)
                return root
        else:
            if not curr.right:
                curr.right = TreeNode(target)
                return root
            else:
                stack.append(curr.right)


# Test Cases
tree = TreeNode(6, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(8))
print(arrayifyTree(insert_bst(tree, 7)) == [
      6, 3, 8, 2, 4, 7])  # [6, 3, 8, 2, 4, 7]
print(arrayifyTree(insert_bst(tree, 5)) == [
      6, 3, 8, 2, 4, 7, 5])  # [6, 3, 8, 2, 4, 7, 5]
print(arrayifyTree(insert_bst(tree, 1)) == [
      6, 3, 8, 2, 4, 7, 1, 5])  # [6, 3, 8, 2, 4, 7, 1, 5]
print(arrayifyTree(insert_bst(None, 1)) == [1])  # [1]

# Given tree:
#              6
#            /   \
#           3     8
#          / \    /
#         2   4  7
#        /     \
#       1       5
