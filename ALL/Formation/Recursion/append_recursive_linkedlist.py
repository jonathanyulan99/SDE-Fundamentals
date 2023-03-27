class ListNode(object):
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def append(head: ListNode, target) -> ListNode:
    if head is None:
        head = ListNode(target)
        return

    if head.next is None:
        head.next = ListNode(target)
        return

    append(head.next, target)


L1 = ListNode(0, ListNode(1))
append(L1, 2)


def printLL(head: ListNode) -> None:
    if not head:
        print(None)
        return
    print(head.value, end='-->')
    printLL(head.next)


printLL(L1)
