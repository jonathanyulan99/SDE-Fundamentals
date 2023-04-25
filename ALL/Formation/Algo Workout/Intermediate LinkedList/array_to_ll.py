from random import randint

class LNode(object):
    def __init__(self,value=None,next=None):
        self.value = value 
        self.next = next 
    
    def print(self):
        curr = self 
        while curr:
            print(curr.value,end='-->')
            curr = curr.next 
        print('Done')

def arrayToLL(array: list[int]) -> LNode:
    sentinnel = LNode(float('inf'))
    curr = sentinnel
    
    for element in array: 
        curr.next = LNode(element) 
        curr = curr.next 
    
    return sentinnel.next 

nums = [randint(x,1000) for x in range(10)]
L2 = arrayToLL(nums)
L2.print()
