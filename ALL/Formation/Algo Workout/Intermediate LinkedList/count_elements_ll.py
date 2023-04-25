class LNode(object):
    def __init__(self,value=0,next=None):
        self.value = value 
        self.next = next 

def count_elements(head:LNode)->int:
    if not head:
        return 0 
    
    return count_elements(head.next) + 1 

L1 = LNode(1,LNode(2,LNode(3)))
L2 = None 
L3 = LNode(1,LNode(2,LNode(3,LNode(4,LNode(5)))))

print(count_elements(L3))