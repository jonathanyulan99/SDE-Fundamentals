class LLNode(object):
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def recursive_min_max(head: LLNode):
    if not head:
        return
    if not head.next:
        return [head.value, head.value]

    def helper(head, _min, _max):
        recursive_min_max(head.next)
        if _min > head.value:
            _min = head.value
        if _max < head.value:
            _max = head.value

    return helper(head, head.value, head.value)


L1 = LLNode(1, LLNode(2, LLNode(3)))
L2 = LLNode(1)
print(recursive_min_max(L1))

'''






'''
