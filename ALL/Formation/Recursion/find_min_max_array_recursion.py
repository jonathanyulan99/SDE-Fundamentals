'''
❓ PROMPT
Given an array, write 2 recursive functions to find the index of the minimum and maximum element in an array. 
If there's a tie-breaker, return the first occurrence.

Example(s)
findMinIndex([12, 1234, 45, 67, 1]) == 4
findMinIndex([10, 20, 30]) == 0
findMinIndex([8, 6, 7, 5, 3, 7]) == 4

findMaxIndex([12, 1234, 45, 67, 1]) == 1
findMaxIndex([10, 20, 30]) == 2
findMaxIndex([8, 6, 7, 5, 3, 7]) == 0
 

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
function findMinIndex(array) {
function findMaxIndex(array) {
def findMinIndex(arr: list[int]) -> int:
def findMaxIndex(arr: list[int]) -> int:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''


def findMinIndex(arr: list[int]) -> int:
    def helper(_min):

        if _min == len(arr)-1:
            return _min

        smallest_index = helper(_min+1)

        if arr[_min] > arr[smallest_index]:
            return smallest_index
        if arr[_min] < arr[smallest_index]:
            return _min

        if arr[_min] == arr[smallest_index]:
            return _min

    return helper(0)


'''
helper(4) : _min = 4 == len(arr) - 1 return _min == 4 
helper(3) : _min = 3 smallest_index=helper(4) returned 4; arr[4] == 1 < arr[_min==3] == 67 return smallest_index= 4
helper(2) : _min = 2 smallest_index=helper(3) returned 4; arr[4] == 1 < arr[_min==2] == 45 return smallest_index= 4
helper(1) : _min = 1 smallest_index=helper(2) returend smallest_index == 4; arr[4] == 1 < arr[_min==1] 1234 return smallest_index = 4
helper(0) : _min = 0 smallest_index=helper(1) returned smallest_index == 4; arr[4] == 1 < arr[_min==0] 12 return smallest_index == 4
findMinIndex([12,1234,45,67,1]) : len(arr) = 5 - 1 = 4 == _min returned 4 
'''

print(findMinIndex([12, 1234, 45, 67, 1]))
# 12 1234 45 67 1
# 1234 45 67 1
# 45 67 1
# 67 1
# 1


def findMaxIndex(arr: list[int]) -> int:
    def helper(max_index):
        if max_index <= 0:
            return max_index

        largest_index = helper(max_index-1)

        if arr[largest_index] > arr[max_index]:
            return largest_index
        if arr[largest_index] < arr[max_index]:
            return max_index

        if arr[largest_index] == arr[max_index]:
            return largest_index

    return helper(len(arr)-1)


print(findMaxIndex([12, 1234, 45, 67, 1]))
print(findMinIndex([12, 1234, 45, 67, 1]) == 4)
print(findMinIndex([10, 20, 30]) == 0)
print(findMinIndex([30, 20, 10]) == 2)
print(findMinIndex([20, 10, 30]) == 1)
print(findMinIndex([10, 20, 30, 10]) == 0)
print(findMinIndex([10, 10, 10, 10]) == 0)
print(findMinIndex([11]) == 0)
print(findMinIndex([8, 6, 7, 5, 3, 7]) == 4)
print(findMinIndex([-10, -5, -3, -30]) == 3)
print(findMinIndex([15, 11]) == 1)
print(findMinIndex([15, 11, 12, 13, 14]) == 1)
print(findMinIndex([15, 17, 16, 12, 13, 14]) == 3)

print(findMaxIndex([12, 1234, 45, 67, 1]) == 1)
print(findMaxIndex([10, 20, 30]) == 2)
print(findMaxIndex([30, 20, 10]) == 0)
print(findMaxIndex([20, 10, 30]) == 2)
print(findMaxIndex([10, 20, 30, 10]) == 2)
print(findMaxIndex([10, 10, 10, 10]) == 0)
print(findMaxIndex([11]) == 0)
print(findMaxIndex([8, 6, 7, 5, 3, 7]) == 0)
print(findMaxIndex([-10, -5, -3, -30]) == 2)
print(findMaxIndex([15, 11]) == 0)
print(findMaxIndex([15, 11, 12, 13, 14]) == 0)
print(findMaxIndex([15, 17, 16, 12, 13, 14]) == 1)
