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