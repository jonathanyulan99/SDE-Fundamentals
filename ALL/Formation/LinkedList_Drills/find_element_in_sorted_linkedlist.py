'''
Q. Given a sorted linked list of unique integers, check if the list contains an element with a target value.

Examples:
• Given a linked list: 2 ➞ 3 ➞ 5, target: 2 // returns True
• Given a linked list: 2 ➞ 3 ➞ 5, target: 4  // returns False
'''


class Node(object):
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


L1 = Node(2, Node(3, Node(5)))


def check_ll(head: Node, target: int) -> bool:
    if not head:
        return False

    while head:
        head_value = head.value
        if target == head_value:
            return True
        head = head.next

    return False


print(check_ll(L1, 5))
LL1 = Node(1, Node(2, Node(3, Node(5, Node(6, Node(7, Node(10)))))))
print(check_ll(None, 1) == False)  # False
print(check_ll(LL1, 2) == True)  # True
print(check_ll(LL1, 4) == False)  # False
print(check_ll(LL1, -1) == False)  # False
print(check_ll(LL1, 10) == True)  # True
print(check_ll(LL1, 11) == False)  # False
