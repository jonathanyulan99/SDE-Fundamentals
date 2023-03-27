'''
❓ PROMPT
Given a linked list of sequential, ascending numbers, return the first missing 
value or the next value that should be in the list. 
For any node, the next value could be 1 or 2 greater than the current node's value.

Furthermore, the list doesn't necessarily begin at 1.

Example(s)
head1 = 1 -> 3
findMissing(head1) == 2

head2 = -3 -> -1
findMissing(head2) == -2

head3 = 5 -> 6 -> 7 -> 8 -> 9
findMissing(head3) == 10

head4 = 5 -> 6 -> 7 -> 8 -> 10
findMissing(head4) == 9
 

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
class Node {
  constructor(val, next=null) {
    this.val = val
    this.next = next
  }
}

function findMissing(head) {

class Node:
  def __init__(self, val, next = None):
    self.val = val
    self.next = next

def findMissing(head: Node) -> int:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def findMissing(head: Node) -> int:
    if not head:
        return 1

    while head.next:
        if head.next.val - head.val > 1:
            return head.val + 1
        head = head.next

    return head.val + 1


head1 = Node(1, Node(3))
head2 = Node(-3, Node(-1))
head3 = Node(5, Node(6, Node(7, Node(8, Node(9)))))
head4 = Node(5, Node(6, Node(7, Node(8, Node(10)))))
head5 = Node(1)
head6 = Node(10)
head7 = Node(1, Node(2))
head8 = Node(5, Node(6, Node(8, Node(9, Node(10)))))
head9 = Node(5, Node(7, Node(8, Node(9, Node(10)))))
head10 = Node(-1)

print(findMissing(head1) == 2)
print(findMissing(head2) == -2)
print(findMissing(head3) == 10)
print(findMissing(head4) == 9)
print(findMissing(head5) == 2)
print(findMissing(head6) == 11)
print(findMissing(head7) == 3)
print(findMissing(head8) == 7)
print(findMissing(head9) == 6)
print(findMissing(head10) == 0)
print(findMissing(None) == 1)
