'''
Q. Given a linked list, sum all elements in the list.

Examples:
• Given a linked list: 1 ➞ 4 ➞ 5 // returns 10
• Given a linked list: 1 // returns 1

'''


class ListNode(object):
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


'''
🔎 EXPLORE
What are some other insightful & revealing test cases?
1. What happens if the linked list is empty?
2. Can the linked list have values that are both negative and positive?
3. What happens if the linked list has only one value?


🧠 BRAINSTORM
What approaches could work?
Algorithm 1: Iterate through the linked list and add to a sum, return sum
Time: O(N)
Space: O(1)


📆 PLAN
Outline of algorithm #:
1. Define a sum variable to hold the sum, have it be zero
2. If the node/head inputted is null/None then return the sum
3. While loop that iterates to the end of the linked list
4. sum is incremented at every step with the linkedlist value
5. move the head to the next poitner it is pointing too
6. return the sum


🛠️ IMPLEMENT
Write your algorithm.


🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''


def sum(node: ListNode) -> int:
    if not node:
        return 0

    sum = 0

    while node:
        sum += node.value
        node = node.next

    return sum


def sum_recursive(node: ListNode) -> int:
    if node is None:
        return 0
    sum = node.value
    sum += sum_recursive(node.next)
    return sum
    # return node.value + sum_recursive(node.next)


print(sum_recursive(ListNode()))  # 0
print(sum(ListNode(0)))  # 0
print(sum(ListNode(0, ListNode(1, ListNode(-1)))))  # 0
print(sum(ListNode(50, ListNode(-50, ListNode(100)))))  # 100
LL1 = ListNode(1, ListNode(4, ListNode(5)))
print(sum(None))  # 0
print(sum(LL1))  # 10
print(sum(ListNode(1)))  # 1
