class ListNode(object):
    def __init__(self, x=None, next=None):
        self.value = x
        self.next = next


'''
❓ PROMPT
Given integers *X* and *Y*, return the head of a linked list with *X* nodes with value *Y*.

Example(s)
createLL(5, 3)
"3 -> 3 -> 3 -> 3 -> 3"

createLL(6, 6)
"6 -> 6 -> 6 -> 6 -> 6 -> 6"

createLL(2, -10)
"-10 -> -10"
 

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
function createLL(count, value) {
def createLL(count: int, val: int) -> Node:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''


def createLL(count: int, val: int) -> ListNode:
    if count <= 0:
        return None

    head = ListNode(val)
    curr = head

    while count > 1:
        curr.next = ListNode(val)
        count -= 1
        curr = curr.next
    return head


def toString(head: ListNode) -> None:
    if not head:
        return "<empty>"

    parts = []
    while head:
        parts.append(str(head.value))
        head = head.next

    return " -> ".join(parts)


print(toString(createLL(0, 1000)) == "<empty>")
print(toString(createLL(1, 999)) == "999")
print(toString(createLL(2, 88)) == "88 -> 88")
print(toString(createLL(3, 4)) == "4 -> 4 -> 4")
print(toString(createLL(5, 3)) == "3 -> 3 -> 3 -> 3 -> 3")
print(toString(createLL(6, 6)) == "6 -> 6 -> 6 -> 6 -> 6 -> 6")
print(toString(createLL(2, -10)) == "-10 -> -10")
print(toString(createLL(3, 0)) == "0 -> 0 -> 0")
