'''
❓ PROMPT
Given a linked list of positive integers, count the elements with odd values from the list. Note that 0 is an even number.

Example(s)
head = 1 -> 1 -> 1 -> 1
countOdd(head) == 4

head = 1 -> 2 -> 3 -> 4
countOdd(head) == 2
 

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
function countOdd(head) {
def countOdd(head: Node) -> int:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''


class Node(object):
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def countOdd(head: Node) -> int:
    if not head:
        return 0

    if head.value % 2 == 1:
        return 1 + countOdd(head.next)
    else:
        return countOdd(head.next)


print(countOdd(None) == 0)

# 0
head = Node(0)
print(countOdd(head) == 0)

# 5
head = Node(5)
print(countOdd(head) == 1)

# 6
head = Node(6)
print(countOdd(head) == 0)

# 1 -> 1 -> 1 -> 1
head = Node(1, Node(1, Node(1, Node(1))))
print(countOdd(head) == 4)

# 1 -> 2 -> 3 -> 4
head = Node(1, Node(2, Node(3, Node(4))))
print(countOdd(head) == 2)

# 2 -> 2 -> 2 -> 2
head = Node(2, Node(2, Node(2, Node(2))))
print(countOdd(head) == 0)

# 1 -> 2 -> 3 -> 4 -> 5
head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(countOdd(head) == 3)

# 6 -> 2 -> 100 -> 4 -> 8
head = Node(6, Node(2, Node(100, Node(4, Node(8)))))
print(countOdd(head) == 0)
