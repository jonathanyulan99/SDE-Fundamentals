def power_of_base(base: int, power: int) -> int:
    # base case when power is 0 then we stop
    if power == 0:
        return 1

    return base * power_of_base(base, power-1)


print(power_of_base(2, 0) == 1)
print(power_of_base(2, 1) == 2)
print(power_of_base(2, 3) == 8)
print(power_of_base(10, 2) == 100)
print(power_of_base(10, 1) == 10)
print(power_of_base(10, 0) == 1)
