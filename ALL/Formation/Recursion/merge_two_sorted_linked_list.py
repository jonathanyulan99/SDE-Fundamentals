class ListNode(object):
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


L1 = ListNode(1, ListNode(3, ListNode(
    5, ListNode(7, ListNode(9, ListNode(11))))))

L2 = ListNode(2, ListNode(4, ListNode(
    6, ListNode(8, ListNode(10, ListNode(12))))))


def print_ll(head: ListNode) -> None:
    while head:
        print(head.value, end='-->')
        head = head.next
    print('None')

# 1->None
# 3->None


def recursive_merge_sort(headA: ListNode, headB: ListNode) -> ListNode:
    # simpliest case is if headA is None or headB is None
    if headA is None:
        return headB
    if headB is None:
        return headA

    if (headA.value < headB.value):
        headA.next = recursive_merge_sort(headA.next, headB)
        # headB = headA
        # return headA
        return headA
    else:
        headB.next = recursive_merge_sort(headA, headB.next)
        # headA = headB
        # return headB
        return headB


L1 = ListNode(1, ListNode(20, ListNode(50)))
L2 = ListNode(1, ListNode(10, ListNode(
    11, ListNode(12, ListNode(13, ListNode(14))))))

print_ll(L1)
print_ll(L2)
L3 = recursive_merge_sort(L1, L2)
print_ll(L3)
