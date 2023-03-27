'''

Q. Given a linked list and a target integer, remove all nodes with the value target.

Examples:
• Given a linked list: 4 ➞ 2 ➞ 3 ➞ 2 ➞ 2, target: 2 // returns 4 ➞ 3
• Given a linked list: 4, target: 4  // returns an empty list

'''


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def arrayify(head) -> list[int]:
    array = []
    ptr = head
    while ptr != None:
        array.append(ptr.value)
        ptr = ptr.next
    return array


def remove(node: ListNode, target: int) -> ListNode:
    # use a sentinnel value
    head = ListNode(float('Inf'))
    # attach the head value to the rest of our LL
    head.next = node
    # assign a curr value to the head sentinnel value we created
    curr = head

    while curr.next:
        if curr.next.value == target:
            curr.next = curr.next.next
        else:
            curr = curr.next

    return head.next


def remove_recursively(node: ListNode, target: int) -> ListNode:
    if not node:
        return None

    node.next = remove_recursively(node.next, target)
    if node.value == target:
        return node.next
    return node


    # Test Cases
LL1 = ListNode(4, ListNode(2, ListNode(
    1, ListNode(1, ListNode(3, ListNode(2, ListNode(2)))))))
LL2 = remove(None, 1)
print(arrayify(LL2))  # []
LL1 = remove(LL1, 1)
print(arrayify(LL1))  # [4, 2, 3, 2, 2]
LL1 = remove(LL1, 2)
print(arrayify(LL1))  # [4, 3]
remove(LL1, 3)
print(arrayify(LL1))  # [4]
LL1 = remove(LL1, 4)
print(arrayify(LL1))  # []

test = remove_recursively(ListNode(1, ListNode(
    2, ListNode(2, ListNode(1, ListNode(2))))), 2)
print(arrayify(test))
