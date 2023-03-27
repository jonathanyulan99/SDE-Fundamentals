'''
Q. Given a linked list and a target integer, remove all nodes with the value target.

Examples:
• Given a linked list: 4 ➞ 2 ➞ 3 ➞ 2 ➞ 2, target: 2 // returns 4 ➞ 3
• Given a linked list: 4, target: 4  // returns an empty list
'''


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def arrayify(head) -> list[int]:
    array = []
    ptr = head
    while ptr != None:
        array.append(ptr.value)
        ptr = ptr.next
    return array


def remove(node: ListNode, target: int) -> ListNode:
    # Write your code here.
    sentinel = ListNode(19999)
    # sentinel.next now points to the head of the linked list
    sentinel.next = node
    # assign a runner to the head of the new linked list
    curr = sentinel

    # this will stop at the
    while curr.next is not None:
        if curr.next.value == target:
            curr.next = curr.next.next
        else:
            curr = curr.next

    return sentinel.next


'''
🔎 EXPLORE
What are some other insightful & revealing test cases?
1. If the target is the sole value in the linked list? -> return empty linked list 
2. If the linked list contains all the same target value? -> return empty linked list
3. If the linked list is emtpy? -> return empty list back 
4. If the target is not in the linked list? -> return the same linkedlist unchained
5. If the target is the head?
6. If the target is the end of the list? 
7. If the target value makes up the last two/or more elements in the list? 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1: Traverse the Linked List and reassign pointers depending on an if condition 
Time: O(N)
Space: O(1)
 
📆 PLAN
Outline of algorithm #: 
1. Check if the node is None, if it is so return back empty 
2. Assign a current pointer to the head of the linkedlist 
3. While loop iterates while curr IS NOT equal to that target value 
4. Let us keep track of the prev value as well 
3.5 1 2 3 4 4 
3.5       T
3.5     P C
3.5     P-->C.next   
3.5         C
3.5     P-->-->None 


🛠️ IMPLEMENT
Write your algorithm.
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''


# Test Cases
LL1 = ListNode(4, ListNode(2, ListNode(
    1, ListNode(1, ListNode(3, ListNode(2, ListNode(2)))))))
# LL2 = remove(None, 1)
# print(arrayify(LL2))  # []
# LL1 = remove(LL1, 1)
# print(arrayify(LL1))  # [4, 2, 3, 2, 2]
# LL1 = remove(LL1, 2)
# print(arrayify(LL1))  # [4, 3]
# remove(LL1, 3)
# print(arrayify(LL1))  # [4]
# LL1 = remove(LL1, 4)
# print(arrayify(LL1))  # []

LL2 = remove(ListNode(1, ListNode(2, ListNode(2))), 1)
print(arrayify(LL2))
