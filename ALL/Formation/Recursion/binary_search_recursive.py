nums = list()
for i in range(15):
    nums.append(i)

nums = [-1, 0, 1, 2, 3, 4, 5, 7, 9, 10, 20]


def binary_search_recursive(lst: list, target: int, left: int, right: int):
    if left > right:
        return (False, -1)

    mid = (left+right) // 2
    if lst[mid] == target:
        return (True, mid)
    if lst[mid] > target:
        return binary_search_recursive(lst, target, left, mid-1)
    return binary_search_recursive(lst, target, mid+1, right)


print(binary_search_recursive(nums, 10, 0, len(nums)-1))
