

class ListNode(object):
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


'''
Q. Given an unsorted linked list, find the element with the largest value.

Examples:
• Given a linked list: 1 ➞ 4 ➞ 5 ➞ 1 // returns 5
• Given a linked list: 1  // returns 1
'''


def find_max(node: ListNode) -> int:
    # Write your code here
    if not node.next:
        return node.value

    if not node:
        return None

    sum = node.value

    prev_sum = find_max(node.next)

    if sum < prev_sum:
        sum = prev_sum

    return sum


def find_max_v2(node: ListNode) -> int:
    if not node:
        return None

    if not node.next:
        return node.value

    return max(node.value, find_max_v2(node.next))


LinkedList1 = ListNode(1, ListNode(50, ListNode(3)))
print(find_max_v2(LinkedList1))
LL1 = ListNode(1, ListNode(4, ListNode(5, ListNode(1))))
LL2 = ListNode(7, ListNode(1, ListNode(5, ListNode(1))))
LL3 = ListNode(-1, ListNode(-3, ListNode(-5, ListNode(0, ListNode(-11)))))
print(find_max(LL1))  # 5
print(find_max(LL2))  # 7
print(find_max(LL3))  # 0
print(find_max(ListNode(1)))  # 1
print(find_max_v2(LL1))  # 5
print(find_max_v2(LL2))  # 7
print(find_max_v2(LL3))  # 0
print(find_max_v2(ListNode(1)))  # 1
