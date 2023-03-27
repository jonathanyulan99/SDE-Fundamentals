import random


def compareTo(first_input, second_inp):
    return first_input < second_inp


def less(v, w):
    return compareTo(v, w)


def exchange(inp_list, index_a, index_b):
    inp_list[index_a], inp_list[index_b] = inp_list[index_b], inp_list[index_a]


print(less(4, 5))

'''
Selection sort. One of the simplest sorting algorithms works as follows:
First, find the smallest item in the array, and exchange it with the first
entry. Then, find the next smallest item and exchange it with the second entry.
Continue in this way until the entire array is sorted. This method is called
selection sort because it works by repeatedly selecting the smallest remaining
item.
'''


def swap(lst, index_a, index_b):
    # store index_a in temp variable
    temp = lst[index_a]
    # index_a now equals index_b
    lst[index_a] = lst[index_b]
    # index_b now equals temp which was index_a
    lst[index_b] = temp


def selection_sort(lst) -> list:
    if not lst:
        assert ("Error No List!")
        return

    for start_index in range(len(lst)):
        minimum_value = start_index

        for rest_indices in range(start_index+1, len(lst)):
            # use the rest_indices in the list to get the smallest value
            if lst[minimum_value] > lst[rest_indices]:
                minimum_value = rest_indices

        # swap now we have the minimum_value with the start_index
        swap(lst, start_index, minimum_value)

    return lst


sample_input = list([9, 4, 2, 3, 5, 6, 8, 1, 7])

print(*sample_input)
print(*selection_sort(sample_input))


def selection_sort_2(inp) -> list:
    assert len(inp) > 0, "No Input"

    for start_index in range(len(inp)):
        minimum_value_index = start_index

        for rest_indices in range(start_index+1, len(inp)):
            if inp[rest_indices] < inp[start_index]:
                minimum_value_index = rest_indices

        inp[start_index], inp[minimum_value_index] = inp[minimum_value_index], inp[start_index]

    return inp


print(*selection_sort_2([9, 4, 2, 3, 5, 6, 8, 1, 7]))

'''
The algorithm that people often use to sort bridge hands is to consider the cards one at a time,
 inserting each into its proper place among those already considered (keeping them sorted). In a 
 computer implementation, we need to make space for the current item by moving larger items one position 
 to the right, before inserting the current item into the vacated position. The following is an 
 implementation of this method, which is called insertion sort.
'''


def insertion_sort(a_list):

    # Traverse through 1 to len(arr)
    for i in range(1, len(a_list)):

        key = a_list[i]

        # Move elements of a_list[0...i-1], that are
        # greater than key, to one position ahead of
        # their current position

        # i starts at 1 then minus 1 = 0
        # starting point
        j = i - 1

        while j >= 0 and key < a_list[j]:
            a_list[j+1] = a_list[j]
            j -= 1
        a_list[j+1] = key


sample_input_3 = ['S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']
insertion_sort(sample_input_3)
print(*sample_input_3)


def insertion_sort_2(inp):
    # base case for inp not having an input
    assert inp, "No Input"

    # base case for a list with only length of 1 is already sorted
    if len(inp) == 1:
        return

    # start at index 1
    # we are going to shift elements to the left of the start_index

    for start_index in range(1, len(inp)):
        # assign temp variable or key
        key = inp[start_index]

        # then we need a variable to hold the moving indices to the left
        shifting_index = start_index - 1

        # use a while loop to keep shifting_index in bounds (>=0)
        # we only shift when the shifting_index element is < than our start_index element
        while shifting_index >= 0 and key < inp[shifting_index]:
            # if the element is less than our start_index element then we perform our swap to the left
            inp[shifting_index+1] = inp[shifting_index]
            # now decrement our shifting index
            shifting_index -= 1
        # once we have done our shifting lets assign our shifting_index with our new key value
        inp[shifting_index+1] = key


insertion_sort_2(sample_input_3)
print(*sample_input_3)


def shell_sort(inp):
    divisor = 2
    length = len(inp)
    gap = length//2

    while gap > 0:
        for i in range(gap, len(inp)):
            key = inp[i]
            j = i

            while j >= gap and inp[j-gap] > key:
                inp[j] = inp[j-gap]
                j -= gap
            inp[j] = key
        gap //= divisor


shell_sort(sample_input_3)
print(*sample_input_3)
