# Write a function that takes a string s as input and checks whether it’s a palindrome or not.
def valid_palindrome(input: str) -> bool:
    if not input:
        return True

    start_pointer = 0
    end_pointer = len(input)-1

    while start_pointer < end_pointer:
        if input[start_pointer] != input[end_pointer]:
            return False
        start_pointer += 1
        end_pointer -= 1

    return True


# Native Approach
def valid_palindrome2(input: str) -> bool:
    return list(input) == list(reversed(input))


print(valid_palindrome('trcrrt'))
