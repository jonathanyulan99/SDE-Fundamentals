# Given an array of integers, nums, and an integer value,
# target, determine if there are any three integers in nums whose
# sum is equal to the target, that is, nums[i] + nums[j] + nums[k] == target.
# Return TRUE if three such integers exist in the array. Otherwise, return FALSE.
def find_sum_of_three(nums: list[int], target: int) -> bool:
    nums.sort()

    for index in range(0, len(nums)-2):
        start_index = index+1
        end_index = len(nums)-1
        while start_index < end_index:
            triplet_sum = nums[start_index] + nums[end_index] + nums[index]
            if target == triplet_sum:
                return True
            elif triplet_sum < target:
                start_index += 1
            else:
                end_index -= 1

    return False


# S R         E
# 1,2,3,4,5,7,8
print(find_sum_of_three([3, 7, 1, 2, 8, 4, 5], 20))
