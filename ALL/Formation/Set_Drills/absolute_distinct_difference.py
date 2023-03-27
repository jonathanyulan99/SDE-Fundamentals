
'''
Given an input array of integer values (positive and negative), return `True` if the absolute value of each element is distinct. Return `False` otherwise.
 

EXAMPLE(S)
[-4, 3, 9, 10, 12] == True because all absolute values are distinct.
[-1, 1] == False because there is a non-distinct absolute value.
[-3, 4, 9, 3, 4] == False because there are 2 non-distinct absolute values: 3 and 4
 

FUNCTION SIGNATURE
def distinctAbsoluteValues(values: list[int]) -> bool:
'''


def distinctAbsoluteValues(values: list[int]) -> bool:
    num_set = set()

    if not values:
        return None

    if len(values) == 1:
        return True

    for x in values:
        if x < 0:
            x *= -1
        if x in num_set:
            return False
        num_set.add(x)

    return True


print(distinctAbsoluteValues([-3, 4, 9, 3, 4]))
