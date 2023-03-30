import time


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
    # Write your code here.
    if node == None:
        return ListNode(target)

    node.next = append(node.next, target)
    return node


# Test Cases

LL1 = ListNode(1, ListNode(4, ListNode(5)))
start_time = time.time()
print(arrayify(append(None, 1)))  # [1]
print(arrayify(append(LL1, 7)))  # [1, 4, 5, 7]
print(arrayify(append(ListNode(), 7)))  # [0, 7]
print(time.time() - start_time)
'''

Q. Given a linked list, append an element with a target value to the list iteratively.

Examples:
• Given a linked list: 1 ➞ 4 ➞ 5, target: 7 // returns 1 ➞ 4 ➞ 5 ➞ 7
• Given a linked list: 0, target 7 // returns 0 ➞ 7


'''


def append2(head: ListNode, value) -> ListNode:
    if head is None:
        # first node in a previously empty list
        return ListNode(value)

    if head.next is None:
        head.next = ListNode(value)
    else:
        append2(head.next, value)

    return head


start_time = time.time()
print(arrayify(append2(None, 1)))  # [1]
print(arrayify(append2(LL1, 7)))  # [1, 4, 5, 7]
print(arrayify(append2(ListNode(), 7)))  # [0, 7]
print(time.time() - start_time)
