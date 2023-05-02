'''
❓ PROMPT
Fold the right side of the binary tree onto the left side of the tree as if it was on a piece of paper with the root at the center of the vertical axis. 
Combine the values when they overlap.

**Hint**: Start out by solving complete trees, then move on to symmetric trees, and finally explore asymmetric trees. Use helper functions to do some of the steps.

Example(s)
        1
    /       \
   2         3
 /   \     /   \
4     5   6     7

Becomes:
     1
    / 
   5
 /   \ 
11   11
 

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
function treeFold(root) {
def treeFold(root: Node) -> Node:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
class Node(object):
    def __init__(self,val=0,left=None,right=None):
        self.val = val 
        self.left = left
        self.right = right 
    
def treeFold(root: Node) -> Node:
    # this function gets called only when their is a right child and not a left child 
    def reverse(root: Node) -> None:
        # if the right also doesn't exsist then we do nothing and just send it back to the previous function call 
        if not root:
            return

        # here we are switching the values at the root.left,root.right = root.right,root.left 
        # because we essentially want to just grab that right node's value and switch it with the left because it doesn't exist 
        # this doesn't matter much for the root.left side as we are going to terminate it anyways when we recursively call back from the call stack 
        root.left, root.right = root.right, root.left

        
        reverse(root.left)
        reverse(root.right)

    def combine(left: Node, right: Node) -> Node:
        # if we have a leftsubtree
        if left:
            # our left.val is easy, its just the left.val = left.val + right.val if there is a right, otherwise we just add 0 
            # the passing of the NONE from our subsequent calls is what changes our right value from NONE to 0 to handle the NULL case 
            left.val += right.val if right else 0
            
            # now we call it again on our combine(left.left,right.right) with the most outside tree, and if right.right doesn't exist then we pass NONE 
            combine(left.left, right.right if right else None)
            
            # here is where we combine the left.right with the right.left utilizing the same logic as above
            # if the right exist then we can pass that value or NONE which will be translated to 0 
            combine(left.right, right.left if right else None)
            
            # Then we need to return our left last call once we have done all the subsequent logic calls, this will be the last call on the stack 
            return left
        
        # if we don't have a left then that means one of our cases forwarded up a NONE as a left input parameter 
        if right:
            
            # this is where we see that we have a right, then we need to call the internal reverse function 
            # passing reverse(right) as the input parameter or subtree 
            reverse(right)
            
            # we need to return right here 
            return right
    
    # this is the line that initaites everything, we don't need to do any work on the root that always stays 
    if root:
        # line that changes our root.left subtree 
        # by calling the internal function combine(root.left,root.right) as the parameters 
        root.left = combine(root.left, root.right)
        # this line gets rid of the root.right subtree which we don't need anymore
        root.right = None

    # return our root back with the modifications made 
    return root
    
def treeFold2(root):
    def reverse(root):
        if not root:
            return 
        
        root.left,root.right = root.right,root.left 
        reverse(root.left)
        reverse(root.right) 
        
    def combine(left,right):
        if left:
            left.val+=right.val if right else 0 
            combine(left.left,right.right if right else None)
            combine(left.right,right.left if right else None)
            return left 
        if right: 
            reverse(right)
            return right 
    if not root:
        return root
    root.left = combine(root.left,root.right)
    root.right = None
    return root 

def compareTrees(a, b):
    if not a and not b:
        return True
    elif not a or not b:
        return False
    else:
        return a.val == b.val \
        and compareTrees(a.left, b.left) \
        and compareTrees(a.right, b.right)

example = Node(1,
  Node(2,
    Node(4),
    Node(5)),
  Node(3,
    Node(6),
    Node(7)))

expectedFolded = Node(1,
  Node(5,
    Node(11),
    Node(11)))
print(compareTrees(treeFold(example), expectedFolded))

print(compareTrees(treeFold(None), None))

single = Node(1)
expectedFolded = Node(1)
print(compareTrees(treeFold(single), expectedFolded))

smallComplete = Node(1,
  Node(2),
  Node(3))

expectedFolded = Node(1,
  Node(5))
print(compareTrees(treeFold(smallComplete), expectedFolded))

symmetric1 = Node(1,
  Node(2, 
    Node(4),
    None),
  Node(3, 
    None, 
    Node(7)))

expectedFolded = Node(1,
  Node(5, 
    Node(11)))
print(compareTrees(treeFold(symmetric1), expectedFolded))

symmetric2 = Node(1,
  Node(2,
    None,
    Node(5)),
  Node(3,
    Node(6),
    None))

expectedFolded = Node(1,
  Node(5,
    None,
    Node(11)))
print(compareTrees(treeFold(symmetric2), expectedFolded))

leftOnly = Node(1,
  Node(2,
    Node(4)))

expectedFolded = Node(1,
  Node(2,
    Node(4)))
print(compareTrees(treeFold2(leftOnly), expectedFolded))

rightOnly = Node(1,
  None,
  Node(2, 
    None,
    Node(4)))

expectedFolded = Node(1,
  Node(2,
    Node(4)))
print(compareTrees(treeFold(rightOnly), expectedFolded))

rightElbow = Node(1,
  None,
  Node(2,
    Node(4)))

expectedFolded = Node(1,
  Node(2,
    None,
    Node(4)))
print(compareTrees(treeFold(rightElbow), expectedFolded))