class Node(object):
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


L1 = Node(1, Node(2, Node(3, Node(4,))))


L2 = Node(1, Node(2, Node(3, Node(4, Node(5)))))

# Make A Cycle Quickly
curr = L2
while curr.next:
    curr = curr.next

curr.next = L2


def is_cycle(head: Node) -> bool:
    if not head:
        return False

    fast, slow = head, head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True

    return False


print(is_cycle(L1))
print(is_cycle(L2))
