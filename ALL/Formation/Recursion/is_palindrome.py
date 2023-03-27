# k
# True

# []
# True

# kayak
# True


def is_palindrome(word: str) -> bool:
    def helper(word, start):
        # base case
        if len(word) == 0 or len(word) == 1:
            return True

        if word[0] == word[len(word)-start]:
            return is_palindrome(word[start:len(word)-start])

        return False
    return helper(word, 1)


print(is_palindrome('kayak'))
