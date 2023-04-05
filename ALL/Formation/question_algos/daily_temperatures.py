def dailyTemperatures(temperatures: list[int]) -> list[int]:
    output = [0] * len(temperatures)
    stack = []

    for index in range(len(temperatures)):
        while stack and temperatures[index] > temperatures[stack[-1]]:
            previous_day = stack.pop()
            output[previous_day] = index - previous_day
        stack.append(index)

    return output


print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
