class ListNode(object):
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


'''

Q. Given an unsorted linked list, count the number of elements (iteratively or recursively).

Examples:
• Given a linked list: 1 ➞ 4 ➞ 5 // returns 3
• Given a linked list: 0 // returns 1

B
- No Linked List Returns -1 
- Will We always be given a valid input 
- Linked List can be non-specifically large 
- The list is unsorted, shouldn't matter to prompt

E
- O(N) iteratively 
- O(1) Space 

P
- initalize a counter at 0 
- have a curr pointer pointing to the first node 
- while curr means there is a valid node there
- counter += 1 
- move curr = curr.next 
- return counter

I 
'''


def count_itr(node: ListNode) -> int:
    counter = 0
    curr = node

    while curr:
        counter += 1
        curr = curr.next

    return counter


# Verify
LL1 = ListNode(1, ListNode(4, ListNode(5)))
print(count_itr(None))  # 0
print(count_itr(LL1))  # 3
print(count_itr(ListNode()))  # 1


def count_rec(node: ListNode) -> int:
    if not node:
        return 0

    count = 1
    # return 1 + count_rec(node.next)
    return count + count_rec(node.next)


LL1 = ListNode(1, ListNode(4, ListNode(5)))
print(count_rec(None))  # 0
print(count_rec(LL1))  # 3
print(count_rec(ListNode()))  # 1
