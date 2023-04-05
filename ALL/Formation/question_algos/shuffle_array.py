'''
Given an integer array nums, design an algorithm to randomly shuffle the array. 
All permutations of the array should be equally likely as a result of the shuffling.

Implement the Solution class:

Solution(int[] nums) Initializes the object with the integer array nums.
int[] reset() Resets the array to its original configuration and returns it.
int[] shuffle() Returns a random shuffling of the array.

'''
import random

# Fisher-Yates Algorithm


class Solution:
    def __init__(self, nums: list[int]):
        self.arr = nums

    def reset(self) -> list[int]:
        return self.arr

    def shuffle(self):
        result = self.arr[:]

        # iterate through the array in reverse, we stop once we get to zero not past it
        # starting from the last index, the i'th index
        # shuffle randomly with an index at the front of the array
        # random.randint(0,i-1)
        # this essentially means that we will shuffle with the remaining left side of the array
        # but never with the index we are working on which in this case is our runner
        for index in range(len(result)-1, 0, -1):
            random_index = random.randrange(0, index)
            result[index], result[random_index] = result[random_index], result[index]

        # alternatively
        # iterate through the entire array
        # your random_index will include the index you are at or the second to last index
        # randrange(includes_parameter,not_includes_parameter)
        # when its at the end of the list it basically means that it will only swap with that last index value
        for index in range(len(result)):
            random_index = random.randrange(index, len(result))
            result[index], result[random_index] = result[random_index], result[index]

        return result
