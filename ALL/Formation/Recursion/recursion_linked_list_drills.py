class LLNode(object):
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


L1 = LLNode(1, LLNode(2, LLNode(4, LLNode(5, LLNode(6)))))
L2 = LLNode(1)
L3 = LLNode(0, LLNode(1))

# fibonacci


def fibonacci(num: int) -> int:
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fibonacci(num-1) + fibonacci(num-2)

# length recursive


def rec_linked(head: LLNode) -> int:
    if not head:
        return 0

    return 1 + rec_linked(head.next)

# get max/min of linked_list


def rec_max(head: LLNode) -> int:
    if not head.next:
        return head.value

    return max(head.value, rec_max(head.next))

# get min of linked_list


def rec_min(head: LLNode) -> int:
    if not head.next:
        return head.value

    return min(head.value, rec_min(head.next))

# do sorted insertion


def rec_inserted(head: LLNode, target: int) -> LLNode:
    node = LLNode(target)
    if not head:
        return node
    if head.value < target:
        head.next = rec_inserted(head.next, target)
        return head
    else:
        node.next = head
        return node


# 1-->2-->3--4-->5-->6-->None
test = rec_inserted(L3, 0.5)
while test:
    print(test.value, end='-->')
    test = test.next
print('None')
