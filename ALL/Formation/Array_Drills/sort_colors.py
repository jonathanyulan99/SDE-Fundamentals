def sort_colors(nums: list[int]):
    l, r = 0, len(nums)-1
    i = 0

    while i <= r:
        if nums[i] == 0:
            nums[l], nums[i] = nums[i], nums[l]
            l += 1
        elif nums[i] == 2:
            nums[r], nums[i] = nums[i], nums[r]
            r -= 1
            i -= 1
        i += 1


nums = [2, 1, 0, 2, 1, 0]
sort_colors(nums)
print(*nums)

def bucket_sort(nums:list[int]):
    container = [0,0,0] 

    for x in nums:
        if x == 0:
            container[0] += 1
        elif x == 1:
            container[1] += 1
        else:
            container[2] += 1 

    for x in range(len(nums)):
        c