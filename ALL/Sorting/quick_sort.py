def quick_sort(arr, left, right):
    if left < right:
        partation_point = partation(arr, left, right)
        quick_sort(arr, left, partation_point-1)
        quick_sort(arr, partation_point+1, right)


def partation(arr, left, right):
    pivot = arr[right]
    j = right-1
    i = left

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    return i


nums = [94, 34, 3, 24, 15, 20, 19]
quick_sort(nums, 0, len(nums)-1)
print(*nums)
