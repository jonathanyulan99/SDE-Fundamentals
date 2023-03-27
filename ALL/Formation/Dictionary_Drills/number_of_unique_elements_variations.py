# most frequent elemnt in array
# if there is a tie, pick the largest value

def most_frequent_array(nums: list[int]) -> int:
    num_frequency = {}
    max_frequency = -10000000
    result = int()

    for num in nums:
        if num in num_frequency:
            num_frequency[num] += 1
        else:
            num_frequency[num] = 1

    sorted_num_frequency_view = sorted(
        num_frequency.items(), key=lambda item: item[1])

    for k, v in dict(sorted_num_frequency_view).items():
        if max_frequency < v:
            max_frquency = v
            result = k
        elif max_frequency == v and k > result:
            result = k

    return result

# Least frequent element in array
# Follow-up: In the case of a tie-breaker, pick the largest value.


def least_frequent_array(nums: list[int]) -> int:
    num_frequency = {}
    min_frequency = 100000000
    result = int()

    for num in nums:
        if num in num_frequency:
            num_frequency[num] += 1
        else:
            num_frequency[num] = 1

    sorted_num_frequency_view = sorted(
        num_frequency.items(), key=lambda item: item[1])

    for k, v in dict(sorted_num_frequency_view).items():
        if min_frequency > v:
            min_frequency = v
            result = k
        elif min_frequency == v and k < result:
            result = k

    return result

# Count the number of elements
# with exactly 2 occurrences ([8, 9, 8, 3, 9, 4] returns 2)


def count_occurrences(nums: list[int]) -> int:
    two_occurrences = 0
    two_occurrences_frequency = {}

    for num in nums:
        if num in two_occurrences_frequency:
            two_occurrences_frequency[num] += 1
            if two_occurrences_frequency.get(num) == 2:
                two_occurrences += 1
            elif two_occurrences_frequency.get(num) > 2:
                two_occurrences -= 1
        else:
            two_occurrences_frequency[num] = 1

    return two_occurrences

# Given an array with all number appearing 2 times and one \
# number appearing 3 times, find the number that shows up 3 times.
# implement using a set


def return_3_occurrences(nums: list[int]) -> int:
    nums_occurrences = set()

    for num in nums:
        if num in nums_occurrences:
            nums_occurrences.discard(num)
        else:
            nums_occurrences.add(num)

    return nums_occurrences.pop()

# Follow-up: Given an array with all numbers appearing
# 3 times and one number appearing only twice, find the number
# that only shows up twice. You must use hashsets


def return_2_occurrences(nums: list[int]) -> int:
    nums_occurrences = dict()
    not_result = []

    for num in nums:
        if num in nums_occurrences:
            nums_occurrences[num] += 1
            if nums_occurrences.get(num) == 3:
                not_result.append(num)
        else:
            nums_occurrences[num] = 1

    for num in nums:
        if num not in not_result:
            return num


print(return_2_occurrences([0, 0, 1, 2, 1, 2, 1, 0]))

# lst_nums = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2]
# print(count_occurrences([8, 9, 8, 3, 9, 4, 3, 8, 9, 3]))
