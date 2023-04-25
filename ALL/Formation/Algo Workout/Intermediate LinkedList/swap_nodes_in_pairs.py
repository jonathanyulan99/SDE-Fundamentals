'''
Given a linked list, swap every two adjacent nodes and return its head. 
You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
'''
class ListNode(object):
    def __init__(self,value,next=None):
        self.value = value 
        self.next = next 
    
    def printll(self):
        while self:
            print(self.value,end='->')
            self = self.next 
        print('Done')

def solution(head:ListNode)->ListNode:
    if not head:
        return 

    # 1->2->3->4->None
    # 2->1->4->3->None 
    
    # 1->2->3->None
    # 2->1->3->None 
    
    #S->1

    #S->1->2 
    sentinnel = ListNode(float('inf'))
    prev = sentinnel
    prev.next = head
    
    while head and head.next:
        first_node = head 
        second_node = head.next 
        
        prev.next = second_node 
        first_node.next = second_node.next 
        second_node.next = first_node
        prev = first_node 
        head = first_node.next
        

    return sentinnel.next 

L1 = ListNode(1,ListNode(2,ListNode(3,ListNode(4))))
L1.printll()
L2 = solution(L1)
L2.printll()

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head:                                            # first (head) node exists
            h = head.next                                   # second node
            if h:                                           # second node exists => a pair exists
                h.next, head.next = head, h.next            # swap node pair, first node with second => 'h' is new head
                h.next.next = self.swapPairs(h.next.next)   # recurse on next pair head
                return h                                    # returns the new head of a swapped node pair
        return head                                         # returns when a node pair doesn't exist