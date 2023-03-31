'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

'''


def valid_parenthesis(s: str) -> bool:
    my_stack = []

    if len(s) / 2 == 0:
        return False

    for char in s:
        if char == '(' or char == '[' or char == '{':
            my_stack.append(char)
        else:
            if len(my_stack) == 0:
                return False
            popped = my_stack.pop()
            if char == '}' and popped != '{':
                return False
            elif char == ')' and popped != '(':
                return False
            elif char == ']' and popped != '[':
                return False
    if len(my_stack) != 0:
        return False
    return True
