def add_one(arr: list) -> list:
    positon_stopped = len(arr) - 1
    for x in range(len(arr)-1, -1, -1):
        if arr[x] == 9:
            arr[x] = 0
            positon_stopped = x - 1
        else:
            break
    if positon_stopped < 0:
        arr.insert(0, 1)
    else:
        arr[positon_stopped] += 1
    return arr


def plus_one(arr: list[int]) -> list[int]:
    # [1,2,3]
    # [0]
    # [9]
    # [3,2,1]
    arr.reverse()
    # arr = arr[::-1]
    # because we are reversing the list[int]'s we start our index_i at zero instead of len(lst) - 1
    i = 0
    # we need to add at least a single one
    one = 1

    while i >= 0 and i < len(arr):
        if arr[i] + one > 9:
            arr[i] = 0
        elif arr[i] + one < 10:
            arr[i] += one
            one = 0
        i += 1

    if i + 1 > len(arr) and one == 1:
        arr.insert(i, one)

    arr.reverse()

    return arr


lst = [1, 2, 4, 9, 9, 9]
print(plus_one(lst))
