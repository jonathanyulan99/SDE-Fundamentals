'''Prompt
Given a 2D rectangular matrix, return all of the values in a single, linear array in spiral order. Start at (0, 0) and /
first include everything in the first row. Then down the last column, back the last row (in reverse), and finally up the /
first column before turning right and continuing into the interior of the matrix.'''


class Solution:
    def spiral_traversal(input):
        pass


llist = [[1, 2, 3, 4, 5],
         [6, 7, 8, 9, 10],
         [11, 12, 13, 14, 15],
         [16, 17, 18, 19, 20]]


def sol(start):
    increment = 3
    sum_age = start
    for x in range(1, 5):
        start += increment
        sum_age += start
        print(x, start, sum_age)
    return sum_age


print(4+7+10+13+16)
print(sol(4))
print(121000*0.12)
print(14520/16)
