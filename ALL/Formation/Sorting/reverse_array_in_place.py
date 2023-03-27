'''
❓ PROMPT
Problem Statement: Write a function that takes an array and reverses its elements in place. 
Do not use built-in methods!

Daniel introduces two pointer problem: https://www.loom.com/share/4090423f2aad41efafe30dd09eb025d8

This task is a basic introduction to what is commonly called "two pointer" algorithms. 
They come up often when dealing with data ordered or organized in some way or when we're trying to do something 
with the ordering.

This problem is the latter. The order of the elements in the array at the start doesn't matter, 
but the task is to re-organize the elements so that at the end, the order is the reverse of what it was coming in.

Example(s)
reverse([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1])
 

🔎 EXPLORE
List your assumptions & discoveries:
1. There must be an input 
2. An empty input or one element in the input just returned that same input 
3. The intial order doesn't matter 


Insightful & revealing test cases:
1. [] => []
2. [1] =? [1] 
3. [1,2,3] => [3,2,1]
4. [1,1,2,2] => [2,2,1,1]

🧠 BRAINSTORM
What approaches could work?
Algorithm 1: Reverse Using Two Pointers
Time: O(N)
Space: O(1)
 

📆 PLAN
Outline of algorithm #: 
1. assign begin pointer to 0 
2. assign end pointer to len(arr) - 1 
3. while loop that terminates only if the begin has not crossed the end 
3.5 swap the indices 
4. begin pointer increments 
5. end pointer decrements 
 

🛠️ IMPLEMENT
function reverse(array) {
def reverse(array: list[int]) -> list[int]:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''


def reverse(array: list[int]) -> list[int]:
    start = 0
    end = len(array) - 1

    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1

    return array


print(reverse([]) == [])
print(reverse([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1])
print(reverse([1, 2, 3]) == [3, 2, 1])
print(reverse([1]) == [1])
print(reverse([1, 1, 2, 2]) == [2, 2, 1, 1])
print(reverse([1, 1, 2]) == [2, 1, 1])

print(reverse([]) == [])
print(reverse([5]) == [5])
print(reverse([5, 10]) == [10, 5])
print(reverse([5, 10, 15]) == [15, 10, 5])
print(reverse([5, 10, 15, 20]) == [20, 15, 10, 5])
print(reverse([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1])
