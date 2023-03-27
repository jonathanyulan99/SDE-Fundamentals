class ListNode(object):
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


# 1 2 3
# 2 1 3

# 1 2 3 4
# 2 1 4 3

def swap_values(head: ListNode) -> ListNode:
    if not head.next:
        return head

    curr = head

    while curr and curr.next:
        curr.value, curr.next.value = curr.next.value, curr.value
        curr = curr.next.next

    return head


def print_ll(head: ListNode) -> None:
    while head:
        print(head.value, end='-->')
        head = head.next
    print('NONE')


L1 = ListNode(1, ListNode(2))
L2 = ListNode()
L3 = ListNode(1, ListNode(2, ListNode(3)))
L4 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

print_ll(L4)
L4 = swap_values(L4)
print_ll(L4)
