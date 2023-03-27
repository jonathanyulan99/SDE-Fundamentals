'''
❓ PROMPT
Given an array of unique integers, find all pairs of elements with the minimum absolute difference.
If there are multiple pairs, return them in ascending order.

Example(s)
Input: arr = [1,3,6,10,15]
sorted_input = [1,3,6,10,15]
Output: [[1,3]]
Explanation: There is only 1 pair of elements with a minimum absolute difference of 2.

Input: arr = [3,8,-10,23,19,-4,-14,27]
Input_sorted = arr = [-14,-10,-4,3,8,19,23,27]

Output: [[-14,-10],[19,23],[23,27]]
Explanation: There are 3 pairs of elements with a minimum absolute difference of 4, 
which are listed in ascending order according to the smaller value in the pair.

Input: arr = [4,2,1,3]
Input_sorted = [1,2,3,4]

Output: [[1,2],[2,3],[3,4]]
Explanation: There are 3 pairs of elements with a minimum absolute difference of 1, 
which are listed in ascending order according to the smaller value in the pair.
 

🔎 EXPLORE
List your assumptions & discoveries:
1. Can the Array be Empty?
2. List of Lists must be in sorted order depending on the first element in the list 
3. The first element in the pair is the smallest value in the list 
4. The last element in the return of the pair is the largest value of the list 

Insightful & revealing test cases:
1. [[]]-> Not Possible
2. [[1,2],[2,1]] -> [[1,2],[1,2]]


🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O(N * log N) -> Sort the Array 
Space: O(N) -> Could return the entire list 
 

📆 PLAN
Outline of algorithm #: 
Input: arr = [3,8,-10,23,19,-4,-14,27]
Input_sorted = arr = [-14,-10,-4,3,8,19,23,27]

Output: [[-14,-10],[19,23],[23,27]]
1. Sorting the array helps us keep the return in sorted order 
2. Store a result list to contain all the values of the pairs 
3. We can store the absolute minimum differnce as a big number override this number if we see the first two values 
3. are smaller than the absolute minimum difference we have 
4. Iterate through the list seeing if the minimum number is overriden 
5. If the minimum number is overriden then rewrite that list 
6. If its same number we can append it to our list 
7. If its larger than we can disregard it 
8. Return it at the end of the list 
 

🛠️ IMPLEMENT
function minAbsDiffPairs(arr) {
def minAbsDiffPairs(arr: list[int]) -> list[list[int]]:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
import math


def minAbsDiffPairs(arr: list[int]) -> list[list[int]]:
    arr.sort()
    minimum_difference = math.inf
    result = []

    for i in range(1, len(arr)):
        if (arr[i]-arr[i-1]) < minimum_difference:
            result = [[arr[i-1], arr[i]]]
            minimum_difference = arr[i]-arr[i-1]
        elif (arr[i]-arr[i-1]) == minimum_difference:
            # return in sorted order on the first element
            result.append(([arr[i-1], arr[i]]))

    return result

    # Verify
arr = [1, 3, 6, 10, 15]
print(minAbsDiffPairs(arr) == [[1, 3]])

arr = [3, 8, -10, 23, 19, -4, -14, 27]
print(minAbsDiffPairs(arr) == [[-14, -10], [19, 23], [23, 27]])

arr = [4, 2, 1, 3]
print(minAbsDiffPairs(arr) == [[1, 2], [2, 3], [3, 4]])

arr = [1, 3, 6, 7, 10, 15]
print(minAbsDiffPairs(arr) == [[6, 7]])

arr = [5, 15]
print(minAbsDiffPairs(arr) == [[5, 15]])

arr = [15, 5]
print(minAbsDiffPairs(arr) == [[5, 15]])
