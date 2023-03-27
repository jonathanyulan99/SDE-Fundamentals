'''
❓ PROMPT
Given a linked list, return the number of values that occur exactly twice.

Example(s)
head = 1 -> 2 -> 2 -> 3 -> 3 -> 3
numPairs(head) == 1


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
function numPairs(head) {
def numPairs(head: Node) -> int:


🧪 VERIFY
Run tests. Methodically debug & analyze issues.

Given a linked list, return the number of values that occur exactly twice.

Example(s)
head = 1 -> 2 -> 2 -> 3 -> 3 -> 3
numPairs(head) == 1


'''


class Node(object):
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def numPairs(head: Node) -> int:
    linked_dict = {}
    count_result = 0

    while head:
        if head.value not in linked_dict:
            linked_dict[head.value] = 1
        else:
            linked_dict[head.value] += 1
            if linked_dict.get(head.value) == 2:
                count_result += 1
            elif linked_dict.get(head.value) == 3:
                count_result -= 1

        head = head.next

    return count_result


L1 = Node(1, Node(2, Node(2, Node(3, Node(3, Node(3, Node(2)))))))
L2 = Node(1, Node(1, Node(2)))
print(numPairs(L2))
head1 = Node(1, Node(2, Node(2, Node(3, Node(3, Node(3))))))
head2 = Node(5, Node(5, Node(10, Node(20))))
head3 = Node(5, Node(5, Node(10, Node(10))))
head4 = Node(5, Node(5, Node(5, Node(10))))
head5 = Node(5, Node(10, Node(10, Node(10))))
head6 = Node(4)
head7 = Node(5, Node(5))
head8 = Node(5, Node(5, Node(5, Node(5))))
head9 = Node(6, Node(9))
head10 = Node(5, Node(5, Node(5, Node(10, Node(10)))))
head11 = Node(6, Node(5, Node(5, Node(5, Node(5, Node(6))))))

print(numPairs(None) == 0)
print(numPairs(head1) == 1)
print(numPairs(head2) == 1)
print(numPairs(head3) == 2)
print(numPairs(head4) == 0)
print(numPairs(head5) == 0)
print(numPairs(head6) == 0)
print(numPairs(head7) == 1)
print(numPairs(head8) == 0)
print(numPairs(head9) == 0)
print(numPairs(head10) == 1)
print(numPairs(head11) == 1)
