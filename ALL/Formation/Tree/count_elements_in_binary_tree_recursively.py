class TreeNode(object):
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# recurisvely
def count_tree(head: TreeNode) -> int:
    if not head:
        return 0

    return count_tree(head.left) + count_tree(head.right) + 1


print(count_tree(None), 0)
print(count_tree(TreeNode(1, TreeNode(2), TreeNode(3))), 3)
print(count_tree(TreeNode(2, TreeNode(29, TreeNode(26)),
      TreeNode(4, None, TreeNode(2, TreeNode(9))))), 6)
print(count_tree(TreeNode()), 1)

'''
                2
            29    4
        26          2
                       9
                       

count_tree(2) ---> count_tree(head.left) ---> 2 + count_tree(head.right) 3 + 1 = 6 
'''
