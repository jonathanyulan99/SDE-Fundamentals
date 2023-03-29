'''
The next greater element of some element x in an array is the first greater 
element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] 
and determine the next greater element of nums2[j] in nums2. If there is no next greater element, 
then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.
'''


def next_greater_element(nums1: list[int], nums2: list[int]) -> list:
    num2_pairing = {}
    stack = list()

    for _n2 in nums2:
        while stack and _n2 > stack[-1]:
            num2_pairing[stack.pop()] = _n2
        stack.append(_n2)

    return [num2_pairing.get(_n1, -1) for _n1 in nums1]


print(next_greater_element([4, 1, 2], [1, 3, 4, 2]))
