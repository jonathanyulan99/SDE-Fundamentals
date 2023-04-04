'''
❓ PROMPT
Given a binary tree, modify each node value to be the sum of itself and its parent node. Return the root node of the modified tree.

Example(s)
       1
   2       4
should turn into
      1
  3       5

       1
   3       4
3   _    _   _
should turn into
       1
   4       5
6    _   _   _
 

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
function immediateParentSum(root) {
def immediateParentSum(root: Node) -> Node:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''


class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def immediateParentSum(root: Node) -> Node:
    if not root:
        return root

    def helper(root, increment):
        if not root:
            return
        if root.left:
            helper(root.left, root.val)
        if root.right:
            helper(root.right, root.val)

        root.val += increment
        return root

    return helper(root, 0)


print(immediateParentSum(None) == None)

#    1
#  1   2
# 3 4    6
root = Node(1,
            Node(1,
                 Node(3),
                 Node(4)
                 ),
            Node(2,
                 None,
                 Node(6)
                 )
            )
immediateParentSum(root)
print(root.val == 1)
print(root.left.val == 2)
print(root.left.left.val == 4)
print(root.left.right.val == 5)
print(root.right.val == 3)
print(root.right.right.val == 8)

#     9
#  3     11
# 1 5  10
root = Node(9,
            Node(3,
                 Node(1),
                 Node(5)
                 ),
            Node(11,
                 Node(10)
                 )
            )
immediateParentSum(root)
print(root.val == 9)
print(root.left.val == 12)
print(root.left.left.val == 4)
print(root.left.right.val == 8)
print(root.right.val == 20)
print(root.right.left.val == 21)

#  1
# 2 4
root = Node(1,
            Node(2),
            Node(4)
            )
immediateParentSum(root)
print(root.val == 1)
print(root.left.val == 3)
print(root.right.val == 5)

#    1
#  3   4
# 3
root = Node(1,
            Node(3,
                 Node(3)
                 ),
            Node(4)
            )
immediateParentSum(root)
print(root.val == 1)
print(root.left.val == 4)
print(root.right.val == 5)
print(root.left.left.val == 6)

root = Node(9)
immediateParentSum(root)
print(root.val == 9)
