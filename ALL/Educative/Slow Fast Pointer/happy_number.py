'''

Write an algorithm to determine if a number, n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return TRUE if n is a happy number, and FALSE if not.

'''


def sum_of_digits(n: int) -> int:
    total_sum = 0
    while n > 0:
        digit = n % 10
        total_sum += digit ** 2
        n = n // 10
    return total_sum


def is_happy_number(n: int) -> bool:
    # initialize a variable slow with the input number
    slow = n
    # initialize a variable fast with the squared sum of the input number's digits
    fast = sum_of_digits(n)

    # if fast is not 1 and also not equal to slow, increment slow by one iteration
    # and fast by two iterations. Essentially, set slow to Sum of Digits(slow) and fast to
    while fast != 1 and fast != slow:
        slow = sum_of_digits(slow)
        fast = sum_of_digits(sum_of_digits(fast))

    if fast == 1:
        return True
    return False

    # if fast converges to 1, return True, otherwise return False


print(is_happy_number(4))
