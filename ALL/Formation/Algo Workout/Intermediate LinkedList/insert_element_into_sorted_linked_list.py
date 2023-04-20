'''
Q. Given a sorted linked list, insert an element in the appropriate position.

Examples:
• Given a linked list: 1 ➞ 3 ➞ 4, target: 2 // returns 1 ➞ 2 ➞ 3 ➞ 4
• Given an empty linked list, target: 1  // returns 1
'''
class ListNode(object):
    def __init__(self,value=0,next=None):
        self.value = value 
        self.next = next 

def arrayify(head) -> list[int]:
    array = []
    ptr = head
    while ptr != None:
        array.append(ptr.value)
        ptr = ptr.next
    return array

def insert(head: ListNode, target: int) -> ListNode:
    # Write your code here
    if not head: 
        return ListNode(target)
    
    curr = head
    prev = None 
    while curr and curr.value <= target:
        prev = curr
        curr = curr.next 
        
    if not prev:
        new_head = ListNode(target)
        new_head.next = head 
        return new_head 
    
    if curr: 
        prev.next = ListNode(target)
        prev = prev.next 
        prev.next = curr 
    else:
        prev.next = ListNode(target) 
    
    return head 

#Try to do a sentinel version
def insert(head: ListNode, target: int) -> ListNode:
    # Write your code here
    if not head: 
        return ListNode(target)
    
    #make sentinel 
    sentinel = ListNode(float('inf'))
    sentinel.next = head 
    curr = sentinel 
    
    while curr:
        if not curr.next or target < curr.next.value: 
            next = curr.next 
            curr.next = ListNode(target) 
            curr.next.next = next 
            break
        curr = curr.next 
    
    return sentinel.next 
            

def insert_rec(head: ListNode, target: int) -> ListNode:
    if not head:
        return ListNode(target)

    if head.value < target: 
        head.next = insert_rec(head.next,target)
    else: 
        new_head = ListNode(target)
        new_head.next = head 
        return new_head 
    
    return head 

LL1 = ListNode(1, ListNode(3, ListNode(4)))
LL2 = ListNode(-3, ListNode(-2, ListNode(-1)))
print(arrayify(insert_rec(LL1, 2))) # [1, 2, 3, 4]
print(arrayify(insert_rec(LL2, -4))) # [-4, -3, -2, -1]
print(arrayify(insert_rec(LL2, 0))) # [-3, -2, -1, 0]
print(arrayify(insert_rec(None, 1))) # [1]