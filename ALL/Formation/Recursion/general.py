def sumArrayMidpointSplit(arr):
    if len(arr) == 1:  # base case
        return arr[0]

    halfway = len(arr)//2
    firstHalf = arr[:halfway]
    secondHalf = arr[halfway:]

    # recursive step
    firstHalfSum = sumArrayMidpointSplit(firstHalf)
    secondHalfSum = sumArrayMidpointSplit(secondHalf)

    # merge step
    return firstHalfSum + secondHalfSum


arr = [5, 5, 5, 5, 10, 10, 10, 20, 20, 10]  # sum = 100

print(sumArrayMidpointSplit(arr))


def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n-1)


print(factorial(5))


def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    return (fibonacci(n-1) + fibonacci(n-2))


print(fibonacci(6))
