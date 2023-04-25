'''
❓ PROMPT
We've been given a list of employees at the company, each person's seniority is denoted by a number, eg: Junior => 3, Senior => 5, and so on.

For each person on the list, we want to find an adjacent employee that outranks them in the list to become their mentor. 
Return a new list of the same length corresponding to the level of the mentor.

If someone can't find an adjacent superior, they should not be assigned a mentor so it should return their own level.

Example(s)
head = 3 -> 1 -> 3
assignMentors(head) == [3,3,3]

head = 5 -> 6 -> 9
assignMentors(head) == [6,9,9]

head = 2 -> 2 -> 2
assignMentors(head) == [2,2,2]

head = 2 -> 7 -> 4 -> 3 -> 5
assignMentors(head) == [7,7,7,5,5]

# Input -> Head of A LinkedList
# Ouput -> List of Integers 

# E: 
    1. Can the input be malinformed? Will the input always be a listNode?
    2. How do we handle for a None/Or ListNode of 1?

# B: 
    T=> O(N): Need to iterate through the LL entirely
    S=> O(N): To store our result 

# P:
    lets use a sentinnel value 
    start at the sentinnel.next 
    check to ensure we have a .next and also check to see we have a current node 
    we only want to check the .next of our current node, not further down our list 
    if the next node's value is not higher than the current node, just continue 
    if the next node's value is higher than the current node, set the current nodes.value to the current_nodes.next.value 
    return our output 
'''
class Node(object):
    def __init__(self,value,next=None):
        self.value = value 
        self.next = next 

# 5->6->9->None 
# 6->6->9 
# 6->9->9
#    P  C         
def assignMentors(head: Node) -> list[int]:
    # assign result 
    result = [] 
    # create sentinnel with a value of smallest 
    sentinnel = Node(float('-inf'))
    sentinnel.next = head
    curr = head
    prev = sentinnel 
    
    if not head:
        return result 
    
    # check to see if there is a current.next
    # if there is a current.next value then we just need to insert that value into our result 
    while curr:
        if curr.next:
            max_result = max(curr.value,prev.value,curr.next.value)
        else:
            max_result = max(curr.value,prev.value)
        result.append(max_result)
        prev = curr
        curr = curr.next 
        
    return result 

def assignMentors(head:Node)->list[int]:
    result = [] 
    sentinnel = Node(float('-inf'))
    sentinnel.next = head 
    prev = sentinnel
    
    while head:
        if head.next:
            max_result = max(head.value,prev.value,head.next.value)
        else:
            max_result = max(head.value,prev.value)
        result.append(max_result) 
        prev = head 
        head = head.next  
    
    return result 

# Verification 
# Empty Case 
print(assignMentors(None))
# LL of length one 
L1 = Node(1) 
print(assignMentors(L1))

# LL where all equal seniority 
L2 = Node(1,Node(1,Node(1)))
print(assignMentors(L2)==[1,1,1])

# LL where highest seniorirty is the beginning and descending order
# LL where the highest seniority is at the end at the order is ascending 
# LL of duplicates 
# LL of all duplicates 
print(assignMentors(None) == None or assignMentors(None) == [])

head = Node(1) # 1
print(assignMentors(head) == [1])

head = Node(3, Node(1, Node(3))) # 3 -> 1 -> 3
print(assignMentors(head) == [3,3,3])

head = Node(5, Node(6, Node(9))) # 5 -> 6 -> 9
print(assignMentors(head) == [6,9,9])

head = Node(2, Node(2, Node(2))) # 2 -> 2 -> 2
print(assignMentors(head) == [2,2,2])

# 2 -> 7 -> 4 -> 3 -> 5
head = Node(2, Node(7, Node(4, Node(3, Node(5)))))
print(assignMentors(head) == [7,7,7,5,5])

# 8 -> 7 -> 5 -> 4 -> 3
head = Node(8, Node(7, Node(5, Node(4, Node(3)))))
print(assignMentors(head) == [8,8,7,5,4])

# 5 -> 6 -> 7 -> 8 -> 9
head = Node(5, Node(6, Node(7, Node(8, Node(9)))))
print(assignMentors(head) == [6,7,8,9,9])

head = Node(9, Node(6, Node(5))) # 9 -> 6 -> 5
print(assignMentors(head) == [9,9,6])