def sum_of_1_to(n: int) -> int:
    if n < 1:
        return -1

    if n == 1:
        return 1

    return n + sum_of_1_to(n-1)


print(sum_of_1_to(5) == 15)
print(sum_of_1_to(1) == 1)
print(sum_of_1_to(10) == 10+9+8+7+6+5+4+3+2+1)
print(sum_of_1_to(0) == -1)
