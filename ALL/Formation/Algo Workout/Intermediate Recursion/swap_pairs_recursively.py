class ListNode(object):
    def __init__(self,value,next=None):
        self.value = value 
        self.next = next 
        
    def print_ll(self):
        while self:
            print(self.value,end='=>')
            self = self.next 
        print('DONE')
        
def swapPairs(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    
    next_node = head.next # 2 4 
    head.next = swapPairs(next_node.next) # 1-> swapPairs(3) #3->swapPairs(5)
    next_node.next = head #4->3
    return next_node #4 

LL = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
LL.print_ll()
LL = swapPairs(LL)
LL.print_ll()
from typing import Optional
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # 1->2->3->None 
        
        # next_node = 2 
        # 
        next_node = head.next
        # 1-> = 2-> == 3
        head.next = self.swapPairs(next_node.next)
        # 2-> 1 -> 3 
        next_node.next = head
        # pass back the 2-> our new head 
        return next_node
#         sentinnel = ListNode(float('inf'))
#         sentinnel.next = head 
#         prev = sentinnel 

#         while head and head.next: 
#             first_node = head 
#             second_node = head.next 

#             prev.next = second_node 
#             first_node.next = second_node.next 
#             second_node.next = first_node
#             prev = first_node 
#             head = first_node.next 
        
#         return sentinnel.next