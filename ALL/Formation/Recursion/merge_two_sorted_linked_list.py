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

# recursive approach 
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

from typing import Optional
# iterative approach
def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if not list1:
        return list2 
    if not list2:
        return list1
    
    curr1 = list1
    curr2 = list2 
    result = ListNode(float('inf'))
    curr = result 
    while curr1 and curr2:
        if curr1.val <= curr2.val:
            curr.next = curr1 
            curr1 = curr1.next 
        else:
            curr.next = curr2
            curr2 = curr2.next 
        curr = curr.next 
    
    while curr1:
        curr.next = curr1
        curr = curr.next
        curr1 = curr1.next 
    
    while curr2:
        curr.next = curr2
        curr = curr.next
        curr2 = curr2.next
    
    return result.next

L1 = ListNode(1, ListNode(20, ListNode(50)))
L2 = ListNode(1, ListNode(10, ListNode(
    11, ListNode(12, ListNode(13, ListNode(14))))))

print_ll(L1)
print_ll(L2)
L3 = recursive_merge_sort(L1, L2)
print_ll(L3)
