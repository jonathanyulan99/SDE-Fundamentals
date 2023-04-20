'''
❓ PROMPT
Given a linked list, delete the middle node of the list in a single pass.

If *n* is the length of the list, the middle node is *n/2* using zero-based indexing.

Return the head of the modified list.

Example(s)
head = 1
deleteMiddleNodeSinglePass(head)) == "<empty>"

head = 1 -> 2
deleteMiddleNodeSinglePass(head)) == "1"

head = 1 -> 2 -> 3
deleteMiddleNodeSinglePass(head)) == "1 -> 3"
 

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
function deleteMiddleNodeSinglePass(head) {
def deleteMiddleNodeSinglePass(head: Node) -> Node:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
class Node(object):
    def __init__(self,value=0,next=None):
        self.value = value 
        self.next = next 

# 1->2->3
def deleteMiddleNodeSinglePass(head: Node) -> Node:
    if not head or not head.next:
        return None 
    
    sentinel = Node(float('inf'))
    sentinel.next = head 
    
    # two pointers 
    slow,fast = sentinel,sentinel
        
    while fast.next and fast.next.next:
        fast = fast.next.next 
        slow = slow.next  
    
    slow.next = slow.next.next 
    
    return head

def deleteMiddleNodeSinglePass(head: Node) -> Node:
    if not head or not head.next:
        return None 
    
    slow,fast = head,head 
    
    while fast and fast.next:
        prev = slow 
        slow = slow.next 
        fast = fast.next.next 
    
    if not fast: 
        prev.next = slow.next 
    else: 
        prev.next = prev.next.next  
    
    return head

L1 = Node(1,Node(2,Node(3)))
L2 = Node(1,Node(2,Node(3,Node(4,Node(5,Node(6))))))
L11 = deleteMiddleNodeSinglePass(L1)
L21 = deleteMiddleNodeSinglePass(L2)
def printLL(head:Node)->None:
    if not head:
        print('None')
        return 
    
    print(head.value,end='->')
    printLL(head.next) 

printLL(L21)
