'''
Write a function that takes a string as input and checks whether it can be a valid palindrome
by removing at most one character from it.
'''


def helper(_str: str, left: int, right: int) -> bool:
    while left < right:
        if _str[left] != _str[right]:
            return False
        left += 1
        right -= 1
    return True


def is_palindrome(s: str) -> bool:
    # initalize two pointers to the end of the string
    l, r = 0, len(s)-1

    while l < r:
        if s[l] != s[r]:
            # skip a character if they aren't equivalent
            # skipL, skipR = s[l+1:r+1], s[l:r]
            # return (skipL == skipL[::-1] or skipR == skipR[::-1])
            return helper(s, l+1, r) or helper(s, l, r-1)
        l, r = l+1, r-1

    return True


print(is_palindrome('abbababa') == True)
print(is_palindrome('abcdeca') == False)
print(is_palindrome('madame') == True)
