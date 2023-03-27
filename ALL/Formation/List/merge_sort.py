def merge_sort(nums: list[int]) -> list:
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    l_half = nums[:mid]
    r_half = nums[mid:]

    left = merge_sort(l_half)
    right = merge_sort(r_half)

    return merge(left, right)


def merge(l: list[int], r: list[int]) -> list:
    result = []
    i = j = 0

    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1

    if j == len(r):
        result += l[i:]
    else:
        result += r[j:]

    return result


nums = [5, 30, 16, -1, -25, 0, 5, 8, 19, 25, 1, 2, -54, 100]
print(merge_sort(nums))
