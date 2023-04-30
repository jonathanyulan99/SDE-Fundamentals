class ListNode(object):
    def __init__(self,value=0,next=None):
        self.value = value 
        self.next = next 
    
    def __repr__(self):
        while self:
            print(str(self.value),end='->')
            self = self.next 
        return 'None'
    
tail = ListNode(-1000)
LL1 = ListNode(1,ListNode(2,ListNode(3,ListNode(4,tail))))
head = ListNode(1000)
head.next = LL1 
tail.next = head 

def find_cycle(head:ListNode)->bool:
    if not head:
        return False 
    
    slow = head
    fast = head 
    
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next 
        if slow is fast:
            return True 
    
    return False 

print(find_cycle(LL1))

LL2 = ListNode(1,ListNode(2,ListNode(3)))

def reverse_linkedlist(head: ListNode)->ListNode:
    if not head:
        return head
    
    curr = head
    prev = None 
    
    while curr: 
        temp = curr.next 
        curr.next = prev 
        prev = curr 
        curr = temp 
    print(prev)
    return prev 

print(LL2)
LL2 = reverse_linkedlist(LL2)
print(LL2)

def reverse_linkedlist(head:ListNode)->ListNode:
    if not head or not head.next:
        return head 

    prev = reverse_linkedlist(head.next)
    head.next.next = head
    head.next = None 
    return prev 

LL2 = reverse_linkedlist(LL2)
print(LL2)