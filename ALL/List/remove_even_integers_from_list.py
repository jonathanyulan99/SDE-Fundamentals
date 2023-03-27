'''
Given a list of size n, remove all even integers from it.
'''

# return something


def remove_even_integers_from_list_return(inp: list) -> list:
    return [value for value in inp if value % 2 != 0]

# remove in-place function


def remove_even_integers_from_list(inp: list) -> None:
    for index, value in enumerate(inp):
        if value % 2 == 0:
            del inp[index]


integers = list(range(13))
odd_integers = remove_even_integers_from_list_return(integers)
print(odd_integers)

remove_even_integers_from_list(integers)
print(integers)


def is_odd(val):
    return val % 2 == 1


integers_2 = list(range(0, 13))
# filter returns a filter object
new_integers_3 = filter(is_odd, integers_2)
new_integers_2 = filter(lambda x: x % 2 == 1, integers_2)
# need to cast the filter object into a list object for easier viewing
print(list(new_integers_2))
print(list(new_integers_3))
