'''
❓ PROMPT
Given a binary tree, find all nodes that have only one child.
Return an array of node values representing each single-child parent in any order.

Example(s)
           1
       2       3
     _   4   _   _
    
should return [2]

           12
       3       4
    1    _   6   _
    
should return [3, 4]

           12
       3       4
    1    _   6   _
  9  _      _ _
    
should return [3, 1, 4]
 

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
function hasSingleChildren(root) {
def hasSingleChildren(root: Node) -> list[int]:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
import collections


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def hasSingleChildren(root: Node) -> list[int]:
    if not root:
        return []

    result = []
    queue = collections.deque([root])

    while queue:

        for i in range(len(queue)):
            node = queue.pop()
            if node.left:
                queue.appendleft(node.left)
            if node.right:
                queue.appendleft(node.right)

            if node.left and not node.right:
                result.append(node.value)
            elif node.right and not node.left:
                result.append(node.value)

    return result


root = Node(12, Node(3, Node(1, Node(9))), Node(4, Node(6)))
print(hasSingleChildren(root))

print(hasSingleChildren(None) == [])

root = Node(1)
print(hasSingleChildren(root) == [])

#   1
# 2
root = Node(1,
            Node(2))
print(set(hasSingleChildren(root)) == set([1]))

#   1
# 2   3
root = Node(1,
            Node(2),
            Node(3))
print(hasSingleChildren(root) == [])

#     1
#  2     3
# _ 4   _ _
root = Node(1,
            Node(2,
                 None,
                 Node(4)),
            Node(3))
print(set(hasSingleChildren(root)) == set([2]))

#     12
#  3     4
# 1 _   6 _
root = Node(12,
            Node(3,
                 Node(1)),
            Node(4,
                 Node(6)))
print(set(hasSingleChildren(root)) == set([3, 4]))

#     12
#   3     4
#  1 _   6  _
# 9 _   _ _
root.left.left.left = Node(9)
print(set(hasSingleChildren(root)) == set([3, 1, 4]))
