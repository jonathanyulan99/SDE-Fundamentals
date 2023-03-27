'''
❓ PROMPT
Given an array and a target count X, return true if there are less than X distinct values in the array.
For example, given [1, 2, 2, 3, 3] and 4, return true because there are only 3 distinct values 1, 2, and 3.

Example(s)
[1, 2, 2, 3, 3], 3 => false (there are exactly 3 distinct values)
[1, 2, 2, 3, 4], 3 => false (there are 4 distinct values)
[1, 1, 2, 2, 2], 3 => true (there are exactly 2 distinct values)
 

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
function fewerThanTargetDistinct(arr, target) {
def fewerThanTargetDistinct(arr: list[int], target: int) -> bool:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''


def fewerThanTargetDistinct(arr: list[int], target: int) -> bool:
    set_container = set()
    counter = 0

    for x in arr:
        if x not in set_container:
            set_container.add(x)
            counter += 1

    return counter < target


print(fewerThanTargetDistinct([1, 2, 2, 3, 3], 3) == False)
print(fewerThanTargetDistinct([1, 2, 2, 3, 4], 3) == False)
print(fewerThanTargetDistinct([1, 1, 2, 2, 2], 3) == True)
print(fewerThanTargetDistinct([1, 2, 2, 3, 3], 3) == False)
print(fewerThanTargetDistinct([1, 2, 2, 3, 4], 3) == False)
print(fewerThanTargetDistinct([1, 1, 2, 2, 2], 3) == True)
print(fewerThanTargetDistinct([9], 1) == False)
print(fewerThanTargetDistinct([9], 2) == True)
print(fewerThanTargetDistinct([8, 8, 8], 1) == False)
print(fewerThanTargetDistinct([8, 8, 8], 2) == True)
print(fewerThanTargetDistinct([8, 8, 8], 3) == True)
print(fewerThanTargetDistinct([6, 7, 8, 9], 1) == False)
print(fewerThanTargetDistinct([6, 7, 8, 9], 2) == False)
print(fewerThanTargetDistinct([6, 7, 8, 9], 3) == False)
print(fewerThanTargetDistinct([6, 7, 8, 9], 4) == False)
print(fewerThanTargetDistinct([6, 7, 8, 9], 5) == True)
