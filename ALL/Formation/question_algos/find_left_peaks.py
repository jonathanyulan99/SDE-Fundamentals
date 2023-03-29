'''
❓ PROMPT
Given an array of integers, return a sub-array of 'Left Peaks'.
A Left Peak is defined as an element that is greater or equal in value to all elements to its right.

Example(s)
find_left_peaks([1, 2, 5, 3, 1, 2]) => [5, 3, 2]
find_left_peaks([3, 2, 1]) => [3, 2, 1]
 

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
function find_left_peaks(arr) {
def find_left_peaks(arr: list[int]) -> list[int]:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''


def find(arr: list[int]) -> list[int]:
    _left_peaks = []

    for idx in range(len(arr)-1, -1, -1):
        if not _left_peaks or _left_peaks[-1] <= arr[idx]:
            _left_peaks.append(arr[idx])

    result = []
    while _left_peaks:
        result.append(_left_peaks.pop())

    return result


# print(find_left_peaks([]) == [])
# print(find_left_peaks([1, 2, 5, 3, 1, 2]) == [5, 3, 1, 2])
# print(find_left_peaks([3, 2, 1]) == [3, 2, 1])
# print(find_left_peaks([1, 2, 3]) == [3])
# print(find_left_peaks([10, 4, 6, 3, 5]) == [10, 4, 6, 3, 5])
# print(find_left_peaks([1, 2, 3, 5, 5, 5, 5, 3, 2, 1])
#       == [5, 5, 5, 5, 3, 2, 1])
# print(find_left_peaks([1, 2, 3, 5, 5, 5, 4, 6, 5, 3, 2, 1]) == [6, 5, 3, 2, 1])
# print(find_left_peaks([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5])


# Traversing the array in reverse
# def find(arr):
#     peak_stack = []

#     for i in range(len(arr) - 1, -1, -1):
#         if not peak_stack or arr[i] >= peak_stack[-1]:
#             peak_stack.append(arr[i])

#     res = [0] * len(peak_stack)
#     i = 0
#     while peak_stack:
#         res[i] = peak_stack.pop()
#         i += 1
#     return res

print(find([]) == [])
print(find([1, 2, 5, 3, 1, 2]) == [5, 3, 2])
print(find([3, 2, 1]) == [3, 2, 1])
print(find([1, 2, 3]) == [3])
print(find([10, 4, 6, 3, 5]) == [10, 6, 5])
print(find([1, 2, 3, 5, 5, 5, 4, 5, 3, 2, 1])
      == [5, 5, 5, 5, 3, 2, 1])
print(find([1, 2, 3, 5, 5, 5, 4, 6, 5, 3, 2, 1]) == [6, 5, 3, 2, 1])
print(find([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5])
