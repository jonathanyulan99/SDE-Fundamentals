'''
❓ PROMPT
Flipping a tree means rotating it 180 degrees around its vertical axis. For example:
     1
   /   \
  2     3
 / \   / \
4  5  6   7

Becomes:
     1
   /   \
  3     2
 / \   / \
7  6  5   4

Example(s)
    5 <--- root
 10   5
flip(root)

root.val == 5
root.left.val == 5
root.right.val == 10

Verify that these are leaf nodes:
root.left.left == None
root.left.right == None
root.right.left == None
root.right.right == None
 

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
function flip(root) {
def flip(root: Node) -> None:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def flip(root: Node) -> None:
    if not root:
        return root

    root.left, root.right = root.right, root.left

    flip(root.left)
    flip(root.right)


root = Node(5)


flip(root)
print(root.val == 5)

#    5
# 10   5
root = Node(5,
            Node(10),
            Node(5))
flip(root)
print(
    root.val == 5,
    root.left.val == 5,
    root.right.val == 10,
    root.left.left == None,  # verify leaf node
    root.left.right == None,  # verify leaf node
    root.right.left == None,  # verify leaf node
    root.right.right == None  # verify leaf node
)

#    6
#  6   6
# 6 6
root = Node(6,
            Node(6,
                 Node(6),
                 Node(6)),
            Node(6))
flip(root)
print(
    root.val == 6,
    root.left.val == 6,
    root.right.val == 6,
    root.left.left == None,  # verify leaf node
    root.left.right == None,  # verify leaf node
    root.right.left.val == 6,
    root.right.right.val == 6,
    root.right.left.left == None,  # verify leaf node
    root.right.left.right == None,  # verify leaf node
    root.right.right.left == None,  # verify leaf node
    root.right.right.right == None  # verify leaf node
)

#     5
#  10   1
# 1  7
root = Node(5,
            Node(10,
                 Node(1),
                 Node(7)),
            Node(1))
flip(root)
print(
    root.val == 5,
    root.left.val == 1,
    root.left.left == None,  # verify leaf node
    root.left.right == None,  # verify leaf node
    root.right.val == 10,
    root.right.left.val == 7,
    root.right.right.val == 1,
    root.right.left.left == None,  # verify leaf node
    root.right.left.right == None,  # verify leaf node
    root.right.right.left == None,  # verify leaf node
    root.right.right.right == None  # verify leaf node
)

#      5
#   2    1
# 3   7   10
#          10
root = Node(5,
            Node(2,
                 Node(3),
                 Node(7)),
            Node(1,
                 None,
                 Node(10,
                      None,
                      Node(10))))
flip(root)
print(
    root.val == 5,
    root.left.val == 1,
    root.left.left.val == 10,
    root.left.right == None,  # verify leaf node
    root.left.left.left.val == 10,
    root.left.left.right == None,  # verify leaf node
    root.left.left.left.left == None,  # verify leaf node
    root.left.left.left.right == None,  # verify leaf node
    root.right.val == 2,
    root.right.left.val == 7,
    root.right.right.val == 3,
    root.right.left.left == None,  # verify leaf node
    root.right.left.right == None,  # verify leaf node
    root.right.right.left == None,  # verify leaf node
    root.right.right.right == None  # verify leaf node
)

#       1
#      2
#     3
#    4
#   5
#  6
# 3
root = Node(1,
            Node(2,
                 Node(3,
                      Node(4,
                           Node(5,
                                Node(6,
                                     Node(3)))))))
flip(root)
print(
    root.val == 1,
    root.left == None,  # verify leaf node
    root.right.val == 2,
    root.right.left == None,  # verify leaf node
    root.right.right.val == 3,
    root.right.right.left == None,  # verify leaf node
    root.right.right.right.val == 4,
    root.right.right.right.left == None,  # verify leaf node
    root.right.right.right.right.val == 5,
    root.right.right.right.right.left == None,  # verify leaf node
    root.right.right.right.right.right.val == 6,
    root.right.right.right.right.right.left == None,  # verify leaf node
    root.right.right.right.right.right.right.val == 3,
    root.right.right.right.right.right.right.left == None,  # verify leaf node
    root.right.right.right.right.right.right.right == None  # verify leaf node
)
