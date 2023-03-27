'''
Implement a function that merges two sorted lists of m and n elements respectively, into another sorted list. 
Name it merge_lists(lst1, lst2).
'''

# returns the original list, no extra memory


def merge_list_2(list_1: list, list_2: list) -> list:
    l1 = l2 = 0

    while l1 < len(list_1) and l2 < len(list_2):
        if list_1[l1] > list_2[l2]:
            list_1.insert(l1, list_2[l2])
            l1 += 1
            l2 += 1
        else:
            l1 += 1

    if l2 < (len(list_2)):
        list_1.extend(list_2[l2:])

    return list_1


test_list = merge_list_2([4, 5, 6], [-2, -1, 0, 7, 9, 10])
print(test_list)

# returns a list, extra memory


def merge_list(list_1: list, list_2: list) -> list:
    new_list = []
    l_1 = l_2 = 0

    while l_1 < len(list_1) and l_2 < len(list_2):
        if list_1[l_1] <= list_2[l_2]:
            new_list.append(list_1[l_1])
            l_1 += 1
        else:
            new_list.append(list_2[l_2])
            l_2 += 1

    while l_1 < len(list_1):
        new_list.append(list_1[l_1])
        l_1 += 1

    while l_2 < len(list_2):
        new_list.append(list_2[l_2])
        l_2 += 1

    return new_list


list_3 = merge_list([4, 5, 6], [-2, -1, 0, 7])
print(list_3)
