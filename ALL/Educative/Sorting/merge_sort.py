def merge_sort(arr: list[int]):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    l_arr = arr[:mid]
    r_arr = arr[mid:]
    l = merge_sort(l_arr)
    r = merge_sort(r_arr)

    return merge(l, r)


def merge(l: list[int], r: list[int]):
    i, j = 0, 0
    result = []

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
