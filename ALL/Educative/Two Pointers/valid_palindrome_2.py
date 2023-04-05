'''
Write a function that takes a string as input and checks whether it can be a valid palindrome
by removing at most one character from it.
'''


def is_palindrome(s: str) -> bool:
    # initalize two pointers to the end of the string
    beg_index = 0
    end_index = len(s)-1
    _mishaps = 0

    while beg_index <= end_index:
        # if the values at the two pointers match move both towards the middle until they meet
        if s[beg_index] == s[end_index]:
            beg_index += 1
            end_index -= 1
        elif s[beg_index] != s[end_index]:
            break

    _beg = beg_index
    _end = end_index
    # skip the first element
    beg_index += 1
    while beg_index <= end_index:
        if s[_beg] == s[_end] and _beg == _end:
            return True
        elif s[beg_index] != s[end_index]:
            _mishaps += 1
        beg_index += 1
        end_index -= 1

    _end -= 1
    while _beg <= _end:
        if s[_beg] == s[_end] and _beg == _end:
            return True
        elif s[_beg] != s[_end]:
            _mishaps += 1
        _beg += 1
        _end -= 1

    return False if _mishaps > 1 else True


print(is_palindrome('abbababa') == True)
print(is_palindrome('abcdeca') == False)
print(is_palindrome('madame') == True)
