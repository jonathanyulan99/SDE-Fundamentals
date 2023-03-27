'''
🔎 EXPLORE
What are some other insightful & revealing test cases?
1. What happens if its just one number?
2. What happens if the array is empty? 
3. What occurs if it's an array of duplicate values?
4. Does this sorting method matter if its based with negative numbers?

1. [] -> ? 
2. [1] -> ?
3. [2,1,1] -> [1,1,2]
4. [10,-2,0] -> [-2,10,0]

🧠 BRAINSTORM
What approaches could work?
Algorithm 1: Insertion Sort 
Time: O(N^2)
Space: O(1)
 

📆 PLAN
Outline of algorithm #: 
- set a 'start' varaible to 1
- iterate to the end of the list 
- inside the first loop assign a variable 'runner' to the same variable as 'start' 
- iterate again from the runner while the runner is in bounds and only when the array[start] > array[runner-1] 
- decrement runner by one to ensure we get through the rest of the sorted array 
 

🛠️ IMPLEMENT
Write your algorithm.
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''


def insertionSort(array: list[int]) -> list[int]:
    for a in range(1, len(array)):
        for b in range(a, 0, -1):
            if array[b] < array[b-1]:
                array[b], array[b-1] = array[b-1], array[b]

    return array


# Test Cases
print(insertionSort([]))  # []
print(insertionSort([1]))  # [1]
print(insertionSort([3, 1, 2, 4]))  # [1, 2, 3, 4]
# [-13, -10, 1, 3, 5, 8, 9, 32]
print(insertionSort([-10, 1, 3, 8, -13, 32, 9, 5]))
