'''
Q. Given K sorted linked lists, merge all the lists into one sorted list. 
Each linked list is sorted in ascending order.

Examples:
• Given a linked list: [] // returns []
• Given an array of linked lists (only the head pointers): 
    [[1, 4, 5], [1, 3, 4], [2, 6]] // returns: [1, 1, 2, 3, 4, 4, 5, 6]
'''
from typing import List
class Node(object):
    def __init__(self,value=0,next=None):
        self.value = value 
        self.next = next 

import heapq

def mergeKLists(lists: list[Node]) -> Node:
  current_head_values = []
  while any(lists):
    for index, LL in enumerate(lists):
      if LL:
        # easy modifications to implement a max_heap
        # heapq.heappush(current_head_values, -LL.value)
        heapq.heappush(current_head_values, LL.value)
        lists[index] = lists[index].next
#   heapq._heapify_max(current_head_values)
  sentinel = Node(0)
  curr = sentinel
  for _ in range(len(current_head_values)):
    # easy modifications to implement a max_heap
    # curr.next = Node(-1*heapq.heappop(current_head_values))
    curr.next = Node(heapq.heappop(current_head_values))
    # heapq._heapify_max(current_head_values)
    curr = curr.next

  return sentinel.next

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists: list[Node]) -> Node:
  if not lists:
    return None
  if len(lists) == 1:
    return lists[0]
  mid = len(lists)//2 # 2
  l, r = mergeKLists(lists[:mid]), mergeKLists(lists[mid:])
  return merge(l, r)

def merge(l, r):
    dummy = p = Node(0)
    while l and r:
        if l.val < r.val:
            p.next = l
            l = l.next
        else:
            p.next = r
            r = r.next
        p = p.next
    p.next = l or r
    return dummy.next

# Test Cases
LL1 = Node(-1, Node(4, Node(5)))
LL2 = Node(1, Node(3, Node(4, Node(4))))
LL3 = Node(2, Node(6))
LL4 = Node(1, Node(11, Node(111)))

test_list = [] 
test_list.append([LL1,LL2,LL3,LL4])
result = mergeKLists([LL1,LL2,LL3,LL4])
while result:
    print(result.val,end=' ')
    result = result.next 
print('None')