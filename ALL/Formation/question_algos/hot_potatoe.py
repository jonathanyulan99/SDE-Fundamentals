import collections


def solution(contestants, passes):
    q = collections.deque(contestants)
    counter = 0

    while len(q) != 1:
        person = q.popleft()
        if counter == passes:
            counter = 0
        else:
            q.append(person)
            counter += 1

    return q.pop()


def solution2(contestants: list, passes: int):
    q = contestants
    counter = 0
    while len(q) != 1:
        person = q.pop(0)
        if passes == counter:
            counter = 0
        else:
            q.append(person)
            counter += 1

    return q.pop()


names = ['jon', 'caitlin', 'adrina']
print(solution2(names, 2))
