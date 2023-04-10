'''
Q. Given a binary tree, count the number of non-leaf nodes (leaf nodes do not have any children).

Q. Given a binary search tree, return the value of the violating node. When there is a violation, return the lowest node. If there is no violating node, return -1.

The properties of a binary search tree are that:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
A violating node occurs when one of these properties is not met.

For example, in this tree:

      5
    /  \
  2    10
   \
    8
We have a violation between 5 and 8 because 8 is not less than 5. Because 8 is the lower node, return 8

Q. Given a binary tree and a depth, remove all nodes that are lower than that depth.

Function Description
replaceNodeValuesBT has the following parameters:

root: the root of the tree
depth: the max depth. This value will be >= 0

Returns:
The root of the tree

Q. Given a binary tree and a target k, count the number of nodes that has a value larger than k

Q. Given a binary tree, count the number of distinct elements in the tree.

     1
   9   5
  1     3
returns 4.

     6
   6   5
  1   6
returns 3.

Q. Construct a zigzag tree from an array (alternating right and left child), starting with right.

Example:
Input: [1, 2, 3, 4, 5]
Output:
          1
            \
              2
             /
          3
            \
              4
             /
          5
'''

