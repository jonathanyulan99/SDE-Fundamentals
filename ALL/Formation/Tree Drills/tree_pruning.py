'''
❓ PROMPT
Given a binary tree and a *target* value, remove the subtrees whose root equals that value. 

As a second step, modify this function to take a function as a parameter instead of a target value. 
The *predicate* function should take a tree node as a parameter and return true if that subtree should be pruned. 
You should test this with a multiple predicate functions to prune in different ways. 
You can start with a predicate function that matches the behavior in the initial problem.

Example(s)
        1 <--- root
    /       \
   2         3
 /   \     /   \
4     5   6     7

Removing the subtree rooted at 3 would result in the following:
     1
    /
   2
 /   \
4     5

prune(root, 3)
root.right == null

A method isEvenValueOver2(node) is passed into this conditional prune.
conditionalPrune(root, isEvenValueOver2)
root.left.left == null
root.right.left == null
 

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
Prune subtrees with a root matching the *target*
function prune(root, target) {
def prune(root: Node, target: int) -> Node:

Prune subtrees with a root matching the criteria from a *predicate* boolean function.
function conditionalPrune(root, predicate) {
def conditionalPrune(root: Node, predicate) -> Node:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''


class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def prune(root: Node, target: int) -> Node:
    if not root or root.val == target:
        return None
    root.left = prune(root.left, target)
    root.right = prune(root.right, target)

    return root


def conditionalPrune(root: Node, predicate) -> Node:
    if not root or predicate(root):
        return None

    root.left = conditionalPrune(root.left, predicate)
    root.right = conditionalPrune(root.right, predicate)

    return root


print(prune(None, 5) == None)

tree = Node(1,
            Node(2,
                 Node(4),
                 Node(5),
                 ),
            Node(3,
                 Node(6),
                 Node(7),
                 ))

sameTree = Node(1,
                Node(2,
                     Node(4),
                     Node(5),
                     ),
                Node(3,
                     Node(6),
                     Node(7),
                     ))


def compareTrees(a, b):
    if not a and not b:
        return True
    elif not a or not b:
        return False
    else:
        return a.val == b.val and \
            compareTrees(a.left, b.left) and \
            compareTrees(a.right, b.right)


prune(tree, 100000)
print(compareTrees(tree, sameTree) == True)
prune(tree, 7)
print(tree.right.right == None)

prune(tree, 3)
print(tree.right == None)

print(prune(tree, 1) == None)

tree = Node(1,
            Node(2,
                 Node(4),
                 Node(5),
                 ),
            Node(3,
                 Node(6),
                 Node(7),
                 ))

sameTree = Node(1,
                Node(2,
                     Node(4),
                     Node(5),
                     ),
                Node(3,
                     Node(6),
                     Node(7),
                     ))


def isEvenValueOver2(node):
    return node.val > 2 and node.val % 2 == 0


def isOddValueOver3(node):
    return node.val > 3 and node.val % 2 == 1


conditionalPrune(tree, isEvenValueOver2)
print(tree.left != None)
print(tree.right != None)
print(tree.left.left == None)
print(tree.right.left == None)
print(tree.left.right != None)
print(tree.right.right != None)

conditionalPrune(tree, isOddValueOver3)
print(tree.left != None)
print(tree.right != None)
print(tree.left.right == None)
print(tree.right.right == None)
