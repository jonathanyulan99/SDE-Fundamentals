from getting_max_number_in_linkedlist import ListNode

L1 = ListNode(1)
curr = L1
for x in range(2, 10):
    curr.next = ListNode(x)
    curr = curr.next


def count(head: ListNode) -> int:
    if not head:
        return 0

    return 1 + count(head.next)


print(count(L1))
