class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def arrayify(head) -> list[int]:
    array = []
    ptr = head
    while ptr != None:
        array.append(ptr.value)
        ptr = ptr.next
    return array


def append(node: ListNode, target: int) -> ListNode:
    if not node:
        return ListNode(target)

    curr = node
    while curr.next is not None:
        curr = curr.next

    curr.next = ListNode(target)
    return node


def append_recursively(node: ListNode, target: int) -> ListNode:
    if not node:
        return ListNode(target)

    node.next = append_recursively(node.next, target)
    return node


'''
🔎 EXPLORE
What are some other insightful & revealing test cases?


🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()


📆 PLAN
Outline of algorithm #:


🛠️ IMPLEMENT
Write your algorithm.


🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

# Test Cases
LL1 = ListNode(1, ListNode(4, ListNode(5)))
print(arrayify(append_recursively(None, 1)))  # [1]
print(arrayify(append_recursively(LL1, 7)))  # [1, 4, 5, 7]
print(arrayify(append_recursively(ListNode(1), 7)))  # [1, 7]
print(arrayify(append_recursively(ListNode(1, ListNode(1)), 7)))  # [1, 1, 7]
