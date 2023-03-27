def decimal_binary_conv(num: int) -> int:
    # base case
    if num <= 0:
        return ''

    return decimal_binary_conv(num//2) + str(num % 2)


print(decimal_binary_conv(233))
