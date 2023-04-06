'''
Find height of tree using recursion (basic)
Find height of tree using BFS (queue)
Find height of tree using DFS (stack)
Find longest continuous path from the root.
'''
from collections import deque


class TNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# remember that the height of all leaf nodes is zero
# height of a tree is defined as the longest path(max) from the root node to the leaf nodes
# height of a node is defined as the longest path(max) from that node to its deepest descendant
# height of a tree == depth of a tree
# BUT height of a node != depth of a node
# height traverses to the leaf nodes
# depth traverses to the root node
def find_height(root: TNode) -> int:
    if not root:
        return -1

    return max(find_height(root.left), find_height(root.right))+1


tree = TNode(1, TNode(2, TNode(4), TNode(5, TNode(8), TNode(9))),
             TNode(3, TNode(6), TNode(7)))
print(find_height(tree))

'''
                1                   height:3    depth:0
        2               3           height:2    depth:1    
    4       5          6 7          height:1    depth:2
           8 9                      height:0    depth:3 
'''


# BFS - Breadth First Search explores ALL the children prior to exploring any deeper
# BFS utilizes a queue versus a stack structure/recrusive nature of DFS
# Deque python's in house for a Queue
# Height of a node: is defined as the longest path from itself, to its deepest descendant being a leaf node
def find_height_using_bfs(root: TNode) -> int:
    _height = -1
    if not root:
        return _height

    queue = deque([root])

    while queue:
        queue_size = len(queue)
        while queue_size > 0:
            # root node is popped
            node = queue.pop()
            queue_size -= 1
            if node.left:
                queue.appendleft(node.left)
            if node.right:
                queue.appendleft(node.right)
        _height += 1
    return _height


print(find_height_using_bfs(tree))


# Find height of tree using DFS (stack)
# height again is defined as the longest path from a specific node to its deepest descendant/leaf node
def find_height_using_dfs(root: TNode) -> int:
    if not root:
        return -1

    # initialize a stack with the root after checking there is a root and a level of default 0
    stack = [(root, 0)]
    # get the max_level as (root,0)[1] => 1
    max_level = stack[-1][1]

    # continue to work through the stack
    while stack:
        # pop at every occurrence, unpacking the tuple
        curr_node, level = stack.pop()
        # we want the deepest descendant so want to take the max between our level and our previous children node's levels
        max_level = max(level, max_level)
        if curr_node.right:
            stack.append((curr_node.right, level+1))
        if curr_node.left:
            stack.append((curr_node.left, level+1))

    return max_level


print(find_height_using_dfs(tree))

# Find longest continuous path from the root.
# Finding the longest path is synonymous with finding the height/max depth of the tree
# In this case we need to be able to traverse the entire tree and check for our max_depth


def find_longest_path_from(root: TNode) -> list:
    if not root:
        return []

    right_subtree = find_longest_path_from(root.right)
    left_subtree = find_longest_path_from(root.left)

    if len(right_subtree) > len(left_subtree):
        right_subtree.insert(0, root.value)
    else:
        left_subtree.insert(0, root.value)

    if len(right_subtree) > len(left_subtree):
        return right_subtree
    return left_subtree


def find_longest_path_from(root: TNode) -> list:
    if not root:
        return ''

    left = str(root.value) + find_longest_path_from(root.left)
    right = str(root.value) + find_longest_path_from(root.right)

    if len(left) < len(right):
        return right
    else:
        return left


print(find_longest_path_from(tree))
