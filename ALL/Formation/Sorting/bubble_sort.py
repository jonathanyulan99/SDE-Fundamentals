'''

Explore 
What are some other insightful & revealing test cases?
1. What happens if its just one number?
2. What happens if the array is empty? 
3. What occurs if it's an array of duplicate values?
4. Does this sorting method matter if its based with negative numbers?


Brainstorm 
What approaches could work?
Algorithm 1: Bubble Sort  
Time: O(N^2)
Space: O(1)

🛠️ IMPLEMENT
Write your algorithm.
1. Outer for loop goes from 1 to the len(array) 
2. Inner for loop goes from 0 to the len(array)-1 
3. if the inner loop array[inner] > array[inner + 1]
3.5 **rememember that you need to increment the inner loops only when comparing because there is no way to move the outer loop
4. swap those values 
5. inner gets incremented 
6. outer gets incremented 
7. return the array 

[2,1] -> [1,2]
[3,2,1] -> [1,2,3]

'''


def bubbleSort(array: list[int]) -> list[int]:
    # if its only one value then its already sorted
    for a in range(1, len(array)):
        # we are comparing the first value to the second value so we need to stop before the last element or we get out of bounds exception
        for b in range(len(array)-a-1):
            if array[b] > array[b+1]:
                array[b], array[b+1] = array[b+1], array[b]

    return array


'''
Verify
'''
# Test Cases
print(bubbleSort([]))  # []
print(bubbleSort([1]))  # [1]
print(bubbleSort([3, 1, 2, 4]))  # [1, 2, 3, 4]
# [-13, -10, 1, 3, 5, 8, 9, 32]
print(bubbleSort([-10, 1, 3, 8, -13, 32, 9, 5]))
