'''
Q. Given a sorted array of unique positive integers and a target integer, check if the array contains a 
target using binary search and return its index. If the array does not contain the target, return -1.

Note:
• Indexes (indices) follow the zero-based numbering rule (i.e. the index of the first element
of an array is 0, not 1). 

Examples:
• Given an array: [1, 2, 3, 6, 8, 13, 113, 153, 200], target: 1 // returns 0
• Given an array: [1, 2, 3, 6, 8, 13, 113, 153, 200], target: 200 // returns 8
• Given an array: [1, 2, 3, 6, 8, 13, 113, 153, 200], target: 154 // returns -1

🔎 EXPLORE
What are some other insightful & revealing test cases?
1. [4,3,2] target: 2 -> Not sorted
2. [] 0 -> No list
3. [1] target:1 -> 0
4. [1] target:2 -> out of bounds
5. [1,2] target: 2 -> 1
6. [1,2,3] target: 1 -> 0

🧠 BRAINSTORM
What approaches could work?
Algorithm 1: Binary Search
Time: O(Log N)
Space: O(1)
 

📆 PLAN
Outline of algorithm #: 
Create variations low and high, representing the range in the array you still have to search. 
Start low at 0 and high at length - 1. While low is less than or equal to high, compute the middle 
index and check that position. Adjust the range base on the results.

🛠️ IMPLEMENT
Write your algorithm.
 
🧪 VERIFY
Run tests. Methodically debug & analyze issues.
'''


def binarySearch(array: list[int], target: int) -> int:
    low = 0
    high = len(array) - 1
    result = -1

    while low <= high:
        mid = (high + low) // 2

        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return result


# Test Cases
array = [1, 2, 3, 6, 8, 13, 113, 153, 200]
print(binarySearch(array, 1))  # 0
print(binarySearch(array, 200))  # 8
print(binarySearch(array, 8))  # 4
print(binarySearch(array, 154))  # -1
