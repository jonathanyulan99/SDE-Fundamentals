class Node(object):
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def _print(self):
        while self:
            print(self.value, end='-->')
            self = self.next
        print('None')


def add_kth_node_from_end(head, k):
    if not head:
        return 0
    i = add_kth_node_from_end(head.next, k) + 1
    if i % k == 0:
        head.value += k
    return i


l1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
l1._print()
add_kth_node_from_end(l1, 2)
l1._print()


'''

Given a linked list of integers and a number, k, add k to every kth node starting from the end. For example, 
if the list is [1 -> 2 -> 3 -> 4] and k is 3, then the result is [1 -> 5 -> 3 -> 4]. 
The 2 was the third value from the end, we added three to get 5. No other nodes are modified.

'''
