'''
function swapValuePairs(head) - swap the data in each node without swapping pointers
'''


class Node(object):
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

# 1->2->3->4->5


def print_ll(head: Node):
    if not head:
        print('Done')
        return
    print(head.value, end='-->')
    print_ll(head.next)


def swap_value_pairs(head: Node):
    if not head:
        return head

    while head and head.next:
        original = head.value
        head.value = head.next.value
        head.next.value = original
        head = head.next.next


L1 = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
L2 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print_ll(L2)
swap_value_pairs(L2)
print_ll(L2)
print_ll(L1)
swap_value_pairs(L1)
print_ll(L1)
print('-------------------------')

'''
function additionNext(head) - add to the value in each node by the value in the next node. 
The tail node has no next node so double its value
'''


def addition_next(head: Node):
    if not head:
        return
    if not head.next:
        head.value *= 2
        return

    head.value += head.next.value
    addition_next(head.next)


L2 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
L1 = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))

print_ll(L2)
addition_next(L2)
print_ll(L2)
print_ll(L1)
addition_next(L1)
print_ll(L1)
print('-------------------------')
'''
function firstRemoveEveryOther(head) - remove every other node starting with removing the head.
'''


def first_remove_every_other_head(head: Node):
    if not head:
        return None

    if not head.next:
        return None

    curr = head.next

    curr.next = first_remove_every_other_head(curr.next)

    return curr


def first_remove_every_other_head(head: Node):
    if not head:
        return head
    if not head.next:
        return None
    curr = head.next

    while curr and curr.next:
        curr.next = curr.next.next
        curr = curr.next

    return head.next


L2 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
L1 = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))

print_ll(L2)
L2 = first_remove_every_other_head(L2)
print_ll(L2)
print_ll(L1)
L1 = first_remove_every_other_head(L1)
print_ll(L1)
print('-------------------------')

'''
function rotateValuesRight(head) - move the values right without altering next pointers. 
The tail's value should become the head's new value.
'''


def rotate_values_right(head: Node):
    if not head:
        return head

    if not head.next:
        return head

    curr = head

    while curr.next:
        curr = curr.next

    curr.next = head
    head = curr
    value_to_stop = curr.value

    while curr.next:
        if curr.next.value == value_to_stop:
            curr.next = None
            return head
        curr = curr.next


def rotate_values_right(head: Node):
    if not head:
        return head

    if not head.next:
        return head

    curr = head
    prev = None
    while curr:
        temp = curr.value
        curr.value = prev
        prev = temp
        curr = curr.next

    head.value = temp
    return head


L2 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
L1 = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))

print_ll(L2)
L2 = rotate_values_right(L2)
print_ll(L2)
print_ll(L1)
L1 = rotate_values_right(L1)
print_ll(L1)
print('-------------------------')

'''
function removeLastQuarterNodes(head) - remove the last 1/4 of the nodes in the linked list. 
How can this be solved without a length variable?
'''


def remove_last_quarter_nodes(head: Node):
    if not head:
        return head

    slow = head
    fast = head

    while fast and fast.next:
        if fast.next.next == None:
            break
        fast = fast.next.next
        slow = slow.next
    slower = slow
    while slow and slow.next:
        slower = slower.next
        slow = slow.next.next
    slower.next = None

    return head


L2 = Node(1, Node(2, Node(
    3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10, Node(11, Node(12))))))))))))
L1 = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(
    9, Node(10, Node(11, Node(12, Node(13, Node(14, Node(15, Node(16))))))))))))))))

print_ll(L2)
L2 = remove_last_quarter_nodes(L2)
print_ll(L2)
print_ll(L1)
L1 = remove_last_quarter_nodes(L1)
print_ll(L1)
print('-------------------------')
