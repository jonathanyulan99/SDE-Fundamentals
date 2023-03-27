'''
❓ PROMPT
Now we're going to apply two different patterns to the same problem and see how the code looks 
and how it affects the runtime.

The task is to determine if an array contains a pair that adds up to a value, k. 
The array is sorted ahead of time.

Just like many problems in computer science and software engineering, there are multiple 
ways to solve the problem, but they often have different time or space complexity, or there are other tradeoffs.

Learning to recognize these decision points is an important step in becoming a strong software engineer.

Patterns and Tools: https://www.loom.com/share/0186a52926dd431bbb25204074812a3a

Example(s)
[1, 5, 8, 10, 13, 18], k = 15 => true
 

🔎 EXPLORE
List your assumptions & discoveries:
1. The array is sorted prior, similiar to binary search 
2. if the largest two values in the array < k then its not in the list 
3. if the smallest two values in the array > k then its not in the list 
4. Negative integers can be an input 

Insightful & revealing test cases:
 1. [] k= any # => False 
 2. [1] k= any # => False 
 3. [1,2] k = 3 => True 
 4. [-1,3] k= 2 => True 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1: Two Pointers 
Time: O(N)
Space: O(1)
 

📆 PLAN
Outline of algorithm #: 
1. Assign start pointer to 0 
2. Assign end pointer to len(array) - 1 
3. While loop to iterate while start is less than end 
4. if condition to checck if the arr[start] + arr[end] = K TRUE condition
5. if sum is greater than K decrement the end pointer
6. if sum is less than K increment the start pointer 
7. if we end the while loop without return of True then we know its FALSE 
 

🛠️ IMPLEMENT
function sumToK(array, k) {
def sumToK(array, k):
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''


def sumToK(array: list[int], K: int) -> bool:
    start = 0
    end = len(array) - 1

    while start < end:
        if array[start]*2 == K:
            return True
        elif array[end]*2 == K:
            return True
        sum = array[start] + array[end]
        if sum == K:
            return True
        elif sum > K:
            end -= 1
        else:
            start += 1

    return False


print(sumToK([], 1) == False)
print(sumToK([1], 1) == False)
print(sumToK([1, 1, 1, 1], 4) == False)
print(sumToK([-1, 2], 1) == True)
print(sumToK([1, 1, 2, 2], 4) == True)
print(sumToK([1, 5, 8, 10, 13, 18], 15) == True)
print(sumToK([1, 1, 8], 16) == True)
print(sumToK([1, 6, 8], 12) == True)
print(sumToK([1, 5, 8, 10, 13, 18], 15) == True)
print(sumToK([1, 5, 8, 10, 13, 18], 12) == False)
print(sumToK([5], 5) == False)
print(sumToK([4], 5) == False)
print(sumToK([], 15) == False)
print(sumToK([2, 2, 5, 8], 4) == True)
print(sumToK([2, 4], 5) == False)
print(sumToK([2, 4], 6) == True)
print(sumToK([4, 4], 7) == False)
print(sumToK([4, 4], 8) == True)
print(sumToK([4, 4, 4, 4], 8) == True)
