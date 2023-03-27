def binary_search(array: list[int], target: int, left: int, right: int) -> int:
    if left > right:
        return -1

    mid = left+((right-left)//2)

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, left, mid-1)
    else:
        return binary_search(array, target, mid+1, right)


def binary_search_primer(array: list[int], target: int) -> int:
    return binary_search(array, target, 0, len(array)-1)


array = [1, 2, 3, 6, 8, 13, 113, 153, 200]
print(binary_search_primer(array, 1))  # 0
print(binary_search_primer(array, 200))  # 8
print(binary_search_primer(array, 8))  # 4
print(binary_search_primer(array, 154))  # -1
