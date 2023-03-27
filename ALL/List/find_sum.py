'''
PROMPT: 
Given a list and a number "k", find two numbers from the list that sum to "k".
'''


def binary_search(lst, searched_value):
    l = 0
    r = len(lst) - 1
    returned = 0

    while l < r:
        m = (l+(r-1))//2

        if lst[m] == searched_value:
            returned = searched_value
        elif lst[m] < searched_value:
            l = m + 1
        else:
            r = m

    if returned != 0:
        return returned
    else:
        return -1

# Output: A list with two integers a and b that add up to k


def find_sum(inp: list, k: int) -> list:
    inp.sort()
    # lst = [1,3,5,6,7,14,21,60]

    for x in lst:
        found = binary_search(inp, k-x)

        if found != -1:
            return [x, found]

    return "No Two Values Are in the list"


def find_sum_2(inp: list, k: int) -> list:
    inp.sort()
    beg, end = 0, len(inp) - 1

    while (beg < end and beg != end):
        if k == inp[beg] + inp[end]:
            return [inp[beg], inp[end]]
        elif k < inp[beg] + inp[end]:
            end -= 1
        else:
            beg += 1

    return "No Two Values Are in the list!"


lst = [1, 2, 3, 4, 5, 5]
k = 10
print(find_sum([1, 2, 3, 4], 5))
print(find_sum([1, 2, 3, 4], 2))
print(find_sum([1, 5, 3], 2))
print(find_sum([1, 2, 3, 4], 5))
