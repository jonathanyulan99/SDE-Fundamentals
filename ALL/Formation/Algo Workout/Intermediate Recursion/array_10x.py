
'''
❓ PROMPT
Given an array of ints, compute recursively if there's a value immediately followed by that value times 10.
We'll use the convention of considering only the part of the array that begins at the given index.
In this way, a recursive call can pass index+1 to move down the array. The initial call will pass in index as 0.

Example(s)
array10x([1, 2, 20], 0) == True
array10x([3, 30], 0) == True
array10x([3], 0) == False
 

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
function array10x(nums, index) {
def array10x(nums: list[int], index: int) -> bool:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
def array10x(nums: list[int], index: int) -> bool:
    if not nums or index == len(nums)-1:
        return False 
    
    if nums[index] * 10 == nums[index+1]: 
        return True 
    
    return array10x(nums,index+1)

print(array10x([1, 2, 20], 0) == True)
print(array10x([3, 30], 0) == True)
print(array10x([3], 0) == False)
print(array10x([], 0) == False)
print(array10x([3, 3, 30, 4], 0) == True)
print(array10x([2, 19, 4], 0) == False)
print(array10x([20, 2, 21], 0) == False)
print(array10x([20, 2, 21, 210], 0) == True)
print(array10x([2, 200, 2000], 0) == True)
print(array10x([0, 0], 0) == True)
print(array10x([1, 2, 3, 4, 5, 6], 0) == False)
print(array10x([1, 2, 3, 4, 5, 50, 6], 0) == True)
print(array10x([1, 2, 3, 4, 5, 51, 6], 0) == False)
print(array10x([1, 2, 3, 4, 4, 50, 500, 6], 0) == True)