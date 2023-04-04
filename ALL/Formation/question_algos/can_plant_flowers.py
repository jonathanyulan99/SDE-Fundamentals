'''
❓ PROMPT
You have a long flowerbed in which some plots are planted and others are not. 
However, new flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty,
and 1 means not empty, and an integer *newFlowers*, return true 
if all *newFlowers* can be planted in the flowerbed without 
violating the no-adjacent-flowers rule.

Example(s)
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

Input: flowerbed = [0,0,1], n = 1
Output: true
 

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
function canPlantFlowers(flowerbed, newFlowers) {
def canPlantFlowers(flowerbed: list[int], newFlowers: int) -> bool:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''


def canPlantFlowers(flowerbed: list[int], newFlowers: int) -> bool:
    # [1,0,0,0,1],n = 2
    # [0,0,1], n =1
    # [1,0,0,0,1], n = 1

    for index, value in enumerate(flowerbed):
        if index == 0 and value == 0:
            if len(flowerbed) == 1:
                flowerbed[index] = 0
                newFlowers -= 1
            else:
                beg = index
                end = index + 1
                if flowerbed[beg] == 0 and flowerbed[end] == 0:
                    flowerbed[beg] = 1
                    newFlowers -= 1

        elif index == len(flowerbed)-1 and value == 0:
            beg = index - 1
            end = index
            if flowerbed[beg] == 0 and flowerbed[end] == 0:
                flowerbed[end] = 1
                newFlowers -= 1

        elif value == 0:
            beg = index - 1
            end = index + 1
            if flowerbed[beg] == 0 and flowerbed[end] == 0:
                flowerbed[index] = 1
                newFlowers -= 1

    return newFlowers <= 0


print(canPlantFlowers([1, 0, 0, 0, 1], 2) == False)
print(canPlantFlowers([1, 0, 0, 0, 1], 1) == True)
print(canPlantFlowers([0, 0, 1], 1) == True)
print(canPlantFlowers([0], 1) == True)
print(canPlantFlowers([0], 2) == False)
print(canPlantFlowers([1], 1) == False)
print(canPlantFlowers([0, 0], 1) == True)
print(canPlantFlowers([0, 0], 2) == False)
print(canPlantFlowers([1, 0], 1) == False)
print(canPlantFlowers([0, 1], 1) == False)
print(canPlantFlowers([1, 1], 1) == False)
print(canPlantFlowers([0, 0, 0], 1) == True)
print(canPlantFlowers([0, 0, 0], 2) == True)
print(canPlantFlowers([0, 0, 0], 3) == False)
print(canPlantFlowers([1, 1, 1, 0, 0], 1) == True)
print(canPlantFlowers([1, 1, 1, 0, 0], 2) == False)
print(canPlantFlowers([1, 1, 1, 1, 1, 1, 1], 0) == True)
print(canPlantFlowers([1, 1, 1, 1, 1, 1, 1], 1) == False)
print(canPlantFlowers([1, 0, 0, 0, 1], 1) == True)
print(canPlantFlowers([1, 0, 0, 0, 1], 2) == False)
print(canPlantFlowers([0, 0, 1], 1) == True)
