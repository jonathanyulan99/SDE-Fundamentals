def sum_natural_numbers(nums: int) -> int:
    if nums == 0:
        return 0

    return nums + sum_natural_numbers(nums-1)


print(sum_natural_numbers(55))
