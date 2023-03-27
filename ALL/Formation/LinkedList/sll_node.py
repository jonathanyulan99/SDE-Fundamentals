class ListNode(object):
    def __init__(self, x=None, next=None):
        self.value = x
        self.next = next


# creating a simple linkedlist data structure
node1 = ListNode(0)
node1.next = ListNode(1)
node2 = ListNode(2)
node1.next.next = node2

# faster way to create a whole linkedlist like above
# with this method there is only one pointer, you access the next nodes using the .next and .next.next attributes
head = ListNode(0, ListNode(1, ListNode(2)))

# how to quickly iterate through a linkedList
# NOTE this while loop terminates when we hit None/null
head = node1
while head:
    print(str(head.value)+'-->', end=' ')
    head = head.next
print("None")

head = node1
while head.next:
    print(str(head.value)+'-->', end=' ')
    # move the pointer
    head = head.next
# Unlike previous example we are at the last node in this example
print(str(head.value)+'--> None')

head = ListNode(10, ListNode(20, ListNode(30)))
# 10 --> 20 --> 30 --> None
# SUM = 60

# Proper way to get the sum in the values our list
sum = head.value + head.next.value + head.next.next.value
print(sum)

# Improper way to get teh sum in the values in our list
try:
    sum = head + head.next + head.next.next
except TypeError:
    print('Error! You are adding the nodes themselves not the nodes values!')
else:
    print(sum)


def sum_llist(head) -> int:
    # tricky base case for a declared but not instantiazed ListNode()
    if head.value is None:
        return 0

    sum = 0

    while head:
        sum += head.value
        head = head.next

    return sum


print(sum_llist(ListNode()))

while head.next:
    print(head.value, end=' ')
    head = head.next
print(head.value)
