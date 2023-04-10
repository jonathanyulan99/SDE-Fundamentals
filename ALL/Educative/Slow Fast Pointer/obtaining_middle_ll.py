class LNode(object):
    def __init__(self,value=0,next=None):
        self.value = value 
        self.next = next 

# 1->2->3->None
# 2->3->None
L1 = LNode(1,LNode(2,LNode(3)))
# 1->2->3-4->None 
# 2->3->4->None
L2 = LNode(1,LNode(2,LNode(3,LNode(4))))

'''
Given a singly linked list, return the middle node of the linked list. 
If the number of nodes in the linked list is even, return the second middle node.
'''
def middle_node_ll(head:LNode)->LNode:
    # check for head of LinkedList
    # return -1 if None 
    if not head:
        return -1 
    
    # assign fast and slow pointers to head 
    fast,slow = head, head 
    
    # traverse the LinkedList 
    # check for fast and fast.next as we as moving that pointer twice as fast 
    # this ensures that if we are to get to the last node, we don't try to traverse 
    # 3->None 
    # head = 3 
    # head.next.next is None pointer which is nothing 
    while fast and fast.next:
        # move slow and fast
        # fast twice as much as slow
        slow = slow.next
        fast = fast.next.next 
        
    return slow 

print(middle_node_ll(L1).value)
print(middle_node_ll(L2).value)
 
        
    