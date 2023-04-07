def index_return_first_occurrence(arr: list[int], target: int) -> int:
    return helper(arr, target, 0)


def helper(arr: list[int], target: int, current_index):
    if len(arr) == current_index:
        # out of bounds haven't found return -1
        return -1
    if arr[current_index] == target:
        return current_index

    return helper(arr, target, current_index+1)


nums = [1, 2, 3, 4, 5, 6]
print(index_return_first_occurrence(nums, 6) == 5)

nums = [6, 5, 4, 3, 2, 1, 6]
print(index_return_first_occurrence(nums, 6) == 0)

nums = [1, 2, 3, 4]
print(index_return_first_occurrence(nums, 6) == -1)
