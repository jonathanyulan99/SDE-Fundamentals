class TNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# DFS -> Depth First Search
# This primarily relies on the use of stacks/recursion normally used
# Stacks due to their LIFO structure permits us to explore depth


def dfs_pre_order_traversal(root: TNode) -> list:
    if not root:
        return []

    result = []

    def DFS(root):
        if not root:
            return

        result.append(root.value)
        DFS(root.left)
        DFS(root.right)
    DFS(root)
    return result


tree = TNode(4, TNode(2, TNode(1), TNode(3)), TNode(6, TNode(5), TNode(7)))
print(dfs_pre_order_traversal(tree))

# 1. DFS -> Depth First Search
# 2. Explore the Depth of the tree fully before backtracking utilizing recursion
# 3. The result array which contains the result of our Tree Node values is outside the scope
# of the recursion so it persist through all the frames
# 4. In-Order Traversal Means that our ROOT of our tree is explored first


def dfs_in_order_traversal(root: TNode) -> list:
    if not root:
        return []

    result = []

    def dfs(root):
        if not root:
            return

        dfs(root.left)
        result.append(root.value)
        dfs(root.right)
    dfs(root)
    return result


print(dfs_in_order_traversal(tree))

# DFS -> Depth First Search
# Utilize Recursion in this example
# Explore fully one subtree before exploring the other
# POST -> means the root node is explored last


def dfs_post_order_traversal(root: TNode) -> list:
    if not root:
        return []

    result = []

    def dfs(root: TNode) -> None:
        if not root:
            return

        dfs(root.left)
        dfs(root.right)
        result.append(root.value)
    dfs(root)

    return result


print(dfs_post_order_traversal(tree))

'''
Let Us Trace The Recursion So That We Can See What is Occuring At each function call frame 
Initial Call: dfs_post_order_traversal(root) result = [] dfs(root)
1st Recursive Frame: dfs(4): dfs(4.left)
2nd Recursive Frame: dfs(2): dfs(2.left)
3rd Recursive Frame: dfs(1): dfs(1.left)
4th Recursive Frame: dfs(None): return 
    3rd Recursive Frame: dfs(1): dfs(1.right)
    4th Recursive Frame: dfs(None): return 
        3rd Recursive Frame: TNode Val:1 result.append(1) return 
            2nd Recursive Frame: dfs(2.right) 
            3rd Recrusive Frame: dfs(3): dfs(3.left)
            4th Recursive Frame: dfs(None): return 
                3rd Recursive Frame: dfs(3.right) 
                4th Recursive Frame: dfs(None): return 
                    3rd Recursive Frame: TNode Val:3 result.append(3) return 
                        2nd Recursive Frame: TNode Val:2 result.append(2) return
                            1st Recursive Frame: dfs(4.right) 
                            2nd Recursive Frame: dfs(6): dfs(6.left) 
                            3rd Recursive Frame: dfs(5): dfs(5.left)
                            4th Recrusive Frame: dfs(None): return 
                                3rd Recursive Frame: dfs(5.left) : dfs(5.right) 
                                4th Recursive Frame: dfs(None): return 
                                    3rd Recursive Frame: TNode Val: 5 result.append(5) return 
                                        2nd Recursive Frame: dfs(6.left): dfs(6.right) 
                                        3rd Reucursive Frame: dfs(7): dfs(7.left)
                                        4th Recursive Frame: dfs(None): return 
                                            3rd recursive Frame: dfs(7.left): dfs(7.right) 
                                            4th recursive Frame: dfs(None): return 
                                                3rd Recursive Frame: TNode Val: 7 result.append(7) return 
                                                    2nd Recurisve Frame: TNode Val: 6 result.append(6) return 
                                                        1st Recursive Frame: TNode Val: 4 result.append(4) return 
                                                            Back To Inital Call return result[1,3,2,5,7,6,4]
Note that Call Stack Never goes past Height of the Tree + 1 (for the original function call that calls the recursive function) 
O(H) but this can be O(N) for space depending on the balancing of the tree 
Time is O(N) because we need to explore all of the TNodes of the tree 
'''
