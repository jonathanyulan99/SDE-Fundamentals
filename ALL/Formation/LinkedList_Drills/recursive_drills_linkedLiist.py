class Node(object):
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


L1 = Node(1, Node(2, Node(3, Node(4))))
print(10/4)


def find_node(head: Node, target):
    if not head:
        return False

    if head.value == target:
        return True

    return find_node(head.next, target)


# not found
print(find_node(L1, 0))
# found
print(find_node(L1, 4))

L2 = Node(1, Node(1, Node(2, Node(2, Node(2, Node(3))))))
print(11/6)


def find_instances(head: Node, target):
    if not head:
        return 0

    if head.value == target:
        return 1 + find_instances(head.next, target)
    return find_instances(head.next, target)


# should return 1
print(find_instances(L2, 3) == 1)
# should return 0
print(find_instances(L1, -1) == 0)
# should return 3
print(find_instances(L2, 2) == 3)


def find_mean(head: Node):
    if not head:
        return -1

    def helper(head, _sum, _count):
        if not head.next:
            return _sum/_count

        return helper(head.next, _sum+head.next.value, _count+1)

    return helper(head, head.value, 1)


print(find_mean(L2))

L3 = Node(1, Node(-1, Node(1, Node(1, Node(-2, Node(-3))))))


def replace_all_negatives_with_zeroes(head: Node):
    if not head:
        return

    if head.value < 0:
        head.value = 0

    replace_all_negatives_with_zeroes(head.next)


def ll_print(head: Node):
    if not head:
        print('Done')
        return
    print(head.value, end=' -> ')
    ll_print(head.next)


ll_print(L3)
replace_all_negatives_with_zeroes(L3)
ll_print(L3)

'''
1->2->3->4->Null


'''


def reverse_linked_list(head: Node):
    if not head or not head.next:
        return head

    prev = reverse_linked_list(head.next)
    head.next.next = head
    head.next = None
    return prev


ll_print(L1)
L1 = reverse_linked_list(L1)
ll_print(L1)


def find_mean(head: Node):
    if not head:
        return -1

    if not head.next:
        return head.value

    def helper(head):
        if not head:
            return (0, 0)

        _sum, _count = helper(head.next)

        _sum += head.value
        _count += 1
        return (_sum, _count)
    _sum, _count = helper(head)

    return _sum / _count


L3 = Node(1, Node(-1, Node(1, Node(1, Node(-2, Node(-3))))))
print(find_mean(L3))
