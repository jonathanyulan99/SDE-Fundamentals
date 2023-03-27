def mostFrequent(nums) -> int:
    if not nums:
        return nums

    if len(nums) == 1:
        return nums[0]

    count_nums = {}
    for num in nums:
        count_nums[num] = count_nums.get(num, 0)+1

    return max([key for key in count_nums if count_nums[key] == max(count_nums.values())])


print(mostFrequent([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 5, 5, 5]))
