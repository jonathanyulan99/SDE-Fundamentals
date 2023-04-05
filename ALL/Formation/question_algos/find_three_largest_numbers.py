'''
❓ PROMPT
Given an array of numbers, return an array of the three largest values.

Example(s)
findThreeLargest([1, 2, 3, 4])
findThreeLargest([1, 2, 3, 27, 4, 5, 35, 6])



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
function findThreeLargest(nums)


🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''


def findThreeLargest(nums: list[int]) -> list[int]:
    if len(nums) <= 3:
        return nums

    upper_bound = float('inf')
    result = []
    for i in range(3):
        largest_value = float('-inf')
        for num in nums:
            if num > largest_value and num < upper_bound:
                largest_value = num
        upper_bound = largest_value
        result.append(largest_value)

    return result


def findThreeLargest(nums: list[int]) -> list[int]:
    if len(nums) <= 3:
        return nums

    nums.sort(reverse=True)
    return nums[0:3]


print(findThreeLargest([]) == [])
print(findThreeLargest([1]) == [1])
print(findThreeLargest([1, 2]) == [1, 2])
print(findThreeLargest([1, 2, 3]) == [1, 2, 3])
print(findThreeLargest([1, 2, 3, 4]) == [4, 3, 2])
