'''
❓ PROMPT
Given a linked list, return an array with all the elements in reverse.

Example(s)
head = 1 -> 3 -> 5 -> 2
createArrayInReverse(head) == [2,5,3,1]
 

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
function createArrayInReverse(node) {
def createArrayInReverse(node: Node) -> list[int]:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
class Node(object):
    def __init__(self,value=0,next=None):
        self.value = value 
        self.next = next 
        
def createArrayInReverse(node: Node) -> list[int]:
    if not node:
        return []
    
    if not node.next:
        return [node.value]
    
    result = createArrayInReverse(node.next) 
    result.append(node.value) 
    
    return result 

L1 = Node(1,Node(2,Node(3,Node(4))))
L2 = Node(1,Node(2,Node(3,Node(4,Node(5)))))
print(createArrayInReverse(L2))
# 1 -> 3 -> 5 -> 2
head = Node(1, Node(3, Node(5, Node(2))))
print(createArrayInReverse(head) == [2, 5, 3, 1])

# 4 -> 9 -> 14
head = Node(4, Node(9, Node(14)))
print(createArrayInReverse(head) == [14, 9, 4])

# 5 -> 10 -> 15 -> 20
head = Node(5, Node(10, Node(15, Node(20))))
print(createArrayInReverse(head) == [20, 15, 10, 5])

# 5
head = Node(5)
print(createArrayInReverse(head) == [5])

# 5 -> 10
head = Node(5, Node(10))
print(createArrayInReverse(head) == [10, 5])

# 5 -> 5 -> 10 -> 10
head = Node(5, Node(5, Node(10, Node(10))))
print(createArrayInReverse(head) == [10, 10, 5, 5])

# 5 -> 5 -> 5
head = Node(5, Node(5, Node(5)))
print(createArrayInReverse(head) == [5, 5, 5])

# 0
head = Node()
print(createArrayInReverse(head) == [0])

# None
head = None
print(createArrayInReverse(head) == [])