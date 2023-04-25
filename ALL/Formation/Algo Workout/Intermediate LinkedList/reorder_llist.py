'''
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
'''
class ListNode(object):
    def __init__(self,value,next=None):
        self.value = value 
        self.next = next 
    
    def printLL(self):
        while self:
            print(self.value,end='->')
            self = self.next 
        print('Done')
        
from typing import Optional
def reorderList( head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow,fast = head,head 
        # get the middle 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
        
        #slow is the middle now 
        prev = None 
        while slow: 
            next_node = slow.next 
            slow.next = prev 
            prev = slow 
            slow = next_node 
        
        # prev is the head of our reversed linkedlist 
        curr = head 
        while prev.next:
            temp = curr.next
            curr.next = prev 
            curr = temp 

            temp = prev.next 
            prev.next = curr
            prev = temp
            
L1 = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
L1.printLL()
reorderList(L1)
L1.printLL()
L2 = ListNode(1,ListNode(2,ListNode(3,ListNode(4))))
L2.printLL()
reorderList(L2)
L2.printLL()