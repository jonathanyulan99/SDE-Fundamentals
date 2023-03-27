def string_reversal(string: str) -> None:
    def helper(string, start):
        if len(string) == 0:
            return ''

        return string[len(string)-start] + helper(string[:len(string)-start], start)
    return helper(string, 1)


input = "the simple engineer"
print((string_reversal(input)))
