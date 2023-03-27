# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

#     def __repr__(self):
#         return str(self.data)


# class Solution:
#     def find_middle(head):

#         if not head:
#             return -1

#         slow = fast = head

#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next

#         return slow.data


# llist = Node(1)
# second = Node("A")
# third = Node(3)


# llist.next = second
# second.next = third


# print(Solution.find_middle(llist))
#       9  6  3  4  1  2  5  8  7
nums = [9, 6, 3, 4, 1, 2, 5, 8, 7]
d = {}
print(d)
for i in range(len(nums)):
    amount = nums[i]
    d.update({amount: i})
print(d)
x = d.keys()
x = sorted(x)

ranking = 1
for val in x:
    idx = d[val]
    nums[idx] = ranking
    ranking += 1

print(*nums)
