def add_binary(num1: str, num2: str) -> str:
    # return the result string
    result = ''
    carry = 0

    num1 = num1[::-1]
    num2 = num2[::-1]

    for i in range(max(len(num1), len(num2))):
        digitA = int(num1[i]) if i < len(num1) else 0
        digitB = int(num2[i]) if i < len(num2) else 0

        total = digitA + digitB + carry
        char = str(total % 2)

        result = char + result
        carry = total // 2

    if carry:
        result = "1" + result

    result = result.lstrip("0")
    return result


# 01001001
#  0110101
#    111 1 110
print(add_binary("01001001", "0110101"))
