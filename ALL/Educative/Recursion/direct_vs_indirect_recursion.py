# Direct Recursion
# Case when the function calls itself within the function
def print_natural_numbers(lower_bound: int, upper_bound: int) -> None:
    if lower_bound > upper_bound:
        print()
        return

    print(lower_bound, end=' ')

    print_natural_numbers(lower_bound+1, upper_bound)


print_natural_numbers(1, 5)


# Indirect Recursion
# Indirect recursion (also called mutual recursion) occurs when a function calls another function until the original function is called, again.
def print_natural_numbers(upper_bound: int) -> None:
    helper(1, upper_bound)


def helper(lower_bound: int, upper_bound: int):
    if lower_bound > upper_bound:
        print()
        return
    print(lower_bound, end=' ')
    return helper(lower_bound+1, upper_bound)

# Also Syntatically can be seen as this


def print_natural_numbers(upper_bound: int) -> None:
    def helper(lower_bound: int, upper_bound: int):
        if lower_bound > upper_bound:
            print()
            return
        print(lower_bound, end=' ')
        return helper(lower_bound+1, upper_bound)
    helper(1, upper_bound)


print_natural_numbers(10)

# Learn How to Draw Recursive Stacks


def printPattern(targetNumber):

    if (targetNumber <= 0):
        print(targetNumber)
        return

    print(targetNumber)
    printPattern(targetNumber - 5)
    print(targetNumber)


# Driver Program
n = 10
printPattern(n)
'''
printPattern(10): print(10) print(10-5) print(10 )
printPattern(5): print(5) print(5-5) print(5) 
printPattern(0): print(0) return 
10
5
0
5
10
'''


def reverse_a_string_rec(s: str) -> str:
    if len(s) == 0:
        return ''

    return reverse_a_string_rec(s[1:]) + s[0]


print(reverse_a_string_rec('OLLEH'))


def count_vowels_in_a_str_rev(s: str) -> int:
    if len(s) == 0:
        return 0

    # vowels = ['a', 'A', 'e', 'E', 'I', 'i', 'o', 'O', 'u', 'U'] using a list
    # use a string more understandable
    vowels = 'aAeEiIoOuU'

    if s[0] in vowels:
        return 1 + count_vowels_in_a_str_rev(s[1:])

    # this creates a new string thus taking up more space let us pass indexes
    return count_vowels_in_a_str_rev(s[1:])


# relies on a helper inside the recursive function to pass the extra paremeters we need to update our s
# stratergy can also be used on arrays, linkedlist, trees
def count_vowels_in_a_str_rev(s: str) -> int:
    def helper(s, max_index):
        if max_index < 0:
            return 0

        vowels = 'aAeEiIoOuU'
        if s[max_index] in vowels:
            return 1 + helper(s, max_index-1)
        return helper(s, max_index-1)
    return helper(s, len(s)-1)


print(count_vowels_in_a_str_rev('Jonathan') == 3)
print(count_vowels_in_a_str_rev('BCDFGH') == 0)
print(count_vowels_in_a_str_rev('Educative') == 5)


def firstIndex(arr, testVariable, currentIndex):
    # Write your code here
    # base case it is out of range
    if currentIndex > len(arr)-1:
        return -1
    # check our first 0 index
    if arr[currentIndex] == testVariable:
        return currentIndex

    # how to check the rest of the arr and increment the index to check 1,2,...N
    return firstIndex(arr, testVariable, currentIndex+1)


print(firstIndex([9, 8, 1, 8, 1, 7], 1, 0) == 2)
print(firstIndex([9, 8, 1, 8, 1, 7], 8, 0) == 1)
print(firstIndex([9, 8, 1, 8, 1, 7], 7, 0) == 5)
print(firstIndex([9, 8, 1, 8, 1, 7], 10, 0) == -1)
