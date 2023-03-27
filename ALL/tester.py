class LLNode(object):
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def addOne(head):
    def helper(head):
        if not head:
            # ONE
            return True

        if helper(head.next):
            head.value += 1

        if head.value == 10:
            head.value = 0
            # TWO
            return True

        # THREE
        return False

    hasCarry = helper(head)
    if hasCarry:
        return LLNode(1, head)

    return head


test1 = LLNode(5, LLNode(4, LLNode(0)))
test2 = addOne(test1)

while test2:
    print(test2.value, end='-->')
    test2 = test2.next
