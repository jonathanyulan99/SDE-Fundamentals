class ListNode(object):
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


L1 = ListNode(1, ListNode(2, ListNode(
    3, ListNode(4, ListNode(5, ListNode(6))))))

# 1-->2-->3-->4-->5-->6-->None


def reverse_linked_list(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head

    end = reverse_linked_list(head.next)
    # head.next.next here is end
    # head here is the previous value after we get to the end of the node
    head.next.next = head
    # break the previous end node chain to ensure we don't create a cycle
    head.next = None
    return end


def print_ll(head: ListNode) -> None:
    while head:
        print(head.value, end='-->')
        head = head.next
    print('None')


print_ll(L1)
L1_reverse = reverse_linked_list(L1)
print_ll(L1_reverse)

array = [1, 2, 3, 4, 5]

L1 = ListNode(100)

for element in array:
    L1.next = ListNode(element)
    L1 = L1.next

print_ll(L1)
