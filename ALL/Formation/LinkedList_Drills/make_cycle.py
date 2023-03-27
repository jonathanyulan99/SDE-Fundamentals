class ListNode(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


def make_cycle(head: ListNode) -> ListNode:
    curr = head
    while curr.next is not None:
        curr = curr.next

    curr.next = head


def printLL(head: ListNode):
    while head:
        print(head.value, end=' ')
        head = head.next


def multiplyNext(head: ListNode) -> ListNode:
    curr = head
    while curr.next:
        curr.value = curr.value * curr.next.value
        curr = curr.next

    curr.value *= curr.value

    return head


L1 = ListNode(2, ListNode(3, ListNode(4)))
multiplyNext(L1)
printLL(L1)
