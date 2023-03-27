def first_repeated(nums: list[int]) -> int:
    if not nums or len(nums) <= 1:
        return None

    container_set = set()

    for x in range(len(nums)):
        if nums[x] in container_set:
            return nums[x]
        else:
            container_set.add(nums[x])

    return None


def first_repeated(nums: list[int]) -> int:
    if not nums or len(nums) <= 1:
        return None

    for x in range(1, len(nums)):
        for y in range(0, len(nums)):
            if x != y and nums[x] == nums[y]:
                return nums[x]

    return None


# empty array
print(first_repeated([]))  # None
# 1 element array
print(first_repeated([1]))  # None
# 2 element array w/ duplcate
print(first_repeated([1, 1]))  # 1
# 2 element array w/o duplicates
print(first_repeated([1, 2]))  # None
# array with multiple duplicates
print(first_repeated([1, 2, 3, 2, 1, 1]))  # 2
# array with an element repeated multiple times
print(first_repeated([1, 0, 2, 5, 6, 8, 1]))  # 1
print(first_repeated([]) == None)
print(first_repeated([5]) == None)
print(first_repeated([5, 5]) == 5)
print(first_repeated([5, 10]) == None)
print(first_repeated([1, 2, 3, 4]) == None)
print(first_repeated([1, 2, 1, 3]) == 1)
print(first_repeated([7, 7, 1, 1]) == 7)
print(first_repeated([2, 8, 8, 8]) == 8)
print(first_repeated([1, 2, 3, 2, 1, 1]) == 2)
