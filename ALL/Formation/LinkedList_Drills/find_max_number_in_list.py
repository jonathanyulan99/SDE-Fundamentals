'''

Q. Given an unsorted linked list, find the element with the largest value.

Examples:
• Given a linked list: 1 ➞ 4 ➞ 5 ➞ 1 // returns 5
• Given a linked list: 1  // returns 1

'''


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def findMax_itr(node: ListNode) -> int:
    if not node:
        return node

    max = -100000000
    curr = node

    while curr:
        if curr.value > max:
            max = curr.value
        curr = curr.next

    return max


LL1 = ListNode(1, ListNode(4, ListNode(5, ListNode(1))))
LL2 = ListNode(7, ListNode(1, ListNode(5, ListNode(1))))
LL3 = ListNode(-1, ListNode(-3, ListNode(15, ListNode(0, ListNode(-11)))))
LL4 = ListNode(-1, ListNode(-3, ListNode(-5,
               ListNode(0, ListNode(-11, ListNode(20))))))
# print(findMax_itr(LL1))  # 5
# print(findMax_itr(LL2))  # 7
# print(findMax_itr(LL3))  # 0
# print(findMax_itr(ListNode(1)))  # 1


def findMax_rec(node: ListNode) -> int:
    if not node:
        # simulate negative infinity
        return -100000000

    max = node.value
    prev_max = findMax_rec(node.next)
    if max < prev_max:
        max = prev_max

    return max


print(findMax_rec(LL1))  # 5
print(findMax_rec(LL2))  # 7
print(findMax_rec(LL3))  # 15
print(findMax_rec(LL4))  # 20
print(findMax_rec(ListNode(1)))  # 1
