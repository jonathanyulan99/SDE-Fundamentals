def sum_list(lst: list) -> int:
    if lst is None:
        return 0
    _sum = 1
    for element in range(len(lst)):
        if isinstance(lst[element], list):
            _sum += sum_list(lst[element])

    return _sum


print(sum_list([1, 2, 3]) == 1)
print(sum_list([1, [1, 2, 3], 3]) == 2)
print(sum_list([1, [1, [1, [1, [1]]]]]) == 5)
print(sum_list([1, [2, 2], [3, 3], [4, 4], 5]) == 4)
print(sum_list([1, [2, [], 2], [3, [6], 3], [4, 4], 5]) == 6)
print(sum_list([[[[[[[[[[[[[]]]]]]]]]]]]]) == 13)
print(sum_list([]) == 1)
print(sum_list([[]]) == 2)
print(sum_list([[], [], []]) == 4)
print(sum_list(None) == 0)
