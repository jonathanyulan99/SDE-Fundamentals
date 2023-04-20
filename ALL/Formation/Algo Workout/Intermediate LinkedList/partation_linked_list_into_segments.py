'''
❓ PROMPT
Given the head of a linked list and any number *parts*, partition the list into *parts* consecutive segments. No two segments should have a size differing more than one.

Return an array of *n* of head nodes. The segments should be in the same original order, and segments occurring earlier should never be smaller than later segments.

Example(s)
list1 = 1->2->3->4->5->6->7->8->9->10->None
segmentLinkedList(list1,1)
Output:
[
  1->2->3->4->5->6->7->8->9->10->None
]

list2 = 1->2->3->4->5->None
segmentLinkedList(list2, parts=10)
Output:
[
  1->None
  2->None
  3->None
  4->None
  5->None
  []
  []
  []
  []
  []
]

list3 = 1->2->3->4->5->None
segmentLinkedList(list3, parts=2)
Output:
[
  1->2->3->None
  4->5->None
]
 
🛠️ IMPLEMENT
def segmentLinkedList(head: Node, parts: int) -> list[Node]:

class Node:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

# converts a list of lists to a string for testing
def toString(arr: list[Node]) -> str:
  if not arr:
    return "[]\n"

  theString = "[\n"
  for head in arr:
    theString += "  " + toStringIndividual(head)
  return theString + "]"

# converts a list to a string for testing
def toStringIndividual(head: Node) -> str:
  if not head:
    return "[]\n"

  theString = ""
  while head:
    theString += str(head.val) + "->"
    head = head.next
  return theString + "None\n"
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
import math 
class Node(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# converts a list of lists to a string for testing
def toString(arr: list[Node]) -> str:
  if not arr:
    return "[]\n"

  theString = "[\n"
  for head in arr:
    theString += "  " + toStringIndividual(head)
  return theString + "]"

# converts a list to a string for testing
def toStringIndividual(head: Node) -> str:
  if not head:
    return "[]\n"

  theString = ""
  while head:
    theString += str(head.val) + "->"
    head = head.next
  return theString + "None\n"

def segmentLinkedList(head: Node, parts: int) -> list[Node]:
    if parts == 1 and not head:
        return [[]] 
    if parts == 1:
        return [head]
    
    def get_length(head,length):
        if not head:
            return length 
        return get_length(head.next,length+1)
    _length = get_length(head,0)
    
    result = [] 
    for i in range(parts):
        if parts > 0 and _length == 0:
            result.append([])
            continue
        partation_amount = math.ceil(_length/(parts-i))
        _length -= partation_amount 
        curr = head 
        original = curr 
        for j in range(1,partation_amount):
            curr = curr.next 
        head = curr.next 
        curr.next = None 
        result.append(original)
    return result 
    


# list1 = Node(1,Node(2,Node(3,Node(4,Node(5,Node(6,Node(7,Node(8,Node(9,Node(10))))))))))
# list2 = Node(1,Node(2,Node(3,Node(4,Node(5)))))
# ans = segmentLinkedList(list2,10)
# for element in ans:
#     while element:
#         print(element.val,end='->')
#         element = element.next 
#     print('None')

print(segmentLinkedList(None, 1)== [[]])
print(segmentLinkedList(None, 2) == [[],[]])

# 1->2->3->4->5->6->7->8->9->10->None
list1 = Node(1, Node(2,Node(3, Node(4, Node(5, Node(
      6, Node(7, Node(8, Node(9, Node(10))))))))))
print(toString(segmentLinkedList(list1, parts=1)) ==
"""[
  1->2->3->4->5->6->7->8->9->10->None
]""")

# 1->2->3->4->5->None
list2 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
# x = segmentLinkedList(list2,parts=10)
# for element in x: 
    # if not isinstance(element,list):
    #     print(element.val)
    # else:
    #     print(element)

print(toString(segmentLinkedList(list2, parts=10)) ==
"""[
  1->None
  2->None
  3->None
  4->None
  5->None
  []
  []
  []
  []
  []
]""")

# 1->2->3->4->5->None
list3 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(toString(segmentLinkedList(list3, parts=2)) ==
"""[
  1->2->3->None
  4->5->None
]""")

# 1->2->3->4->5->None
list4 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(toString(segmentLinkedList(list4, parts=3))==
"""[
  1->2->None
  3->4->None
  5->None
]""")

# 1->2->3->4->5->None
list5 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(toString(segmentLinkedList(list5, parts=5)) ==
"""[
  1->None
  2->None
  3->None
  4->None
  5->None
]""")

# 1->2->3->4->5->6->7->8->9->10->None
list6 = Node(1, Node(2,Node(3, Node(4, Node(5,
Node(6, Node(7, Node(8, Node(9, Node(10))))))))))
print(toString(segmentLinkedList(list6, parts=3)) ==
"""[
  1->2->3->4->None
  5->6->7->None
  8->9->10->None
]""")