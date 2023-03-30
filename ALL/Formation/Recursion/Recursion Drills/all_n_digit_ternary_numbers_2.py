def generateNDigitTernaries(n):
    output = []
    stack = ""

    def permute():
        nonlocal stack
        if len(stack) == n:
            output.append(stack)
        return

        for i in range(3):
            stack += str(i)
            permute()
            stack = stack[:-1]

    # single digit is a special case
    if n == 1:
        output.append('0')

    for i in range(1, 3):
        stack += str(i)
        permute()
        stack = stack[:-1]

    return output
