def fibonacci_sequence(n: int) -> int:
    if n == 0 or n == 1:
        return n

    return fibonacci_sequence(n-1) + fibonacci_sequence(n-2)


print(fibonacci_sequence(0) == 0)
print(fibonacci_sequence(1) == 1)
print(fibonacci_sequence(2) == 1)
print(fibonacci_sequence(7) == 13)
