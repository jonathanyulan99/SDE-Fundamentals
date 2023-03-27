def solution(str):
    d = dict()

    for char in str:
        if char in d:
            d[char] += 1
        else:
            d[char] = 1

    container = []

    d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    d = list(d)
    for x in d:
        container.append(x[0])

    return container
