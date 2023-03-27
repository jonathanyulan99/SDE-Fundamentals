'''
❓ PROMPT
Given an array, create a palindrome linked list by iterating through the array forwards and backwards. *The last element should not be repeated.*

Example(s)
createPalindromeLL([99]) == "99"
createPalindromeLL([1,4,5]) == "1 -> 4 -> 5 -> 4 -> 1"
 

🔎 EXPLORE
List your assumptions & discoveries:
 

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
function createPalindromeLL(arr) {
def createPalindromeLL(arr: list[int]) -> Node:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

Given an array, create a palindrome linked list by iterating through the array forwards and backwards. 
*The last element should not be repeated.*

'''
'''
B: 
- Take an array and transform it into a linkedlist 
- The input can be empty so return an empty LinkeList 
- [1,2,3] => 1->2->3->2->1 len(3) -> len(5) 
- [1,2] => 1->2->1 len(2) -> len(3) 
- len(num) * 2 - 1 = len(palindrome)
'''


class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


def pll(head: Node):
    curr = head
    while curr:
        print(curr.value, end='-->')
        curr = curr.next
    print('None')


def createPalindromeLL(arr: list[int]) -> Node:
    if not arr:
        return

    pal_len = len(arr) * 2 - 1
    l1 = Node('INF')
    l2 = l1
    itr = 0

    while pal_len > 0:
        if pal_len >= len(arr):
            l1.next = Node(arr[itr])
            itr += 1
        elif pal_len < len(arr):
            l1.next = Node(arr[itr-2])
            itr -= 1
        l1 = l1.next
        pal_len -= 1

    return l2.next


test1 = createPalindromeLL([1, 2, 3])
pll(test1)


def toString(head: Node) -> None:
    if not head:
        return "<empty>"

    parts = []
    while head:
        parts.append(str(head.value))
        head = head.next

    return " -> ".join(parts)


print(toString(createPalindromeLL([])) == "<empty>")
print(toString(createPalindromeLL([99])) == "99")
print(toString(createPalindromeLL([4, 2])) == "4 -> 2 -> 4")
print(toString(createPalindromeLL([1, 4, 5])) == "1 -> 4 -> 5 -> 4 -> 1")
print(toString(createPalindromeLL([4, 9, 14])) == "4 -> 9 -> 14 -> 9 -> 4")
print(toString(createPalindromeLL([20, 15, 10, 5]))
      == "20 -> 15 -> 10 -> 5 -> 10 -> 15 -> 20")
print(toString(createPalindromeLL([5, 5, 5, 5]))
      == "5 -> 5 -> 5 -> 5 -> 5 -> 5 -> 5")
print(toString(createPalindromeLL([1, 2, 3, 2, 1]))
      == "1 -> 2 -> 3 -> 2 -> 1 -> 2 -> 3 -> 2 -> 1")
