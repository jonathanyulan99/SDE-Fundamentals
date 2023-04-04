'''
❓ PROMPT
Given an array and a target count X, return the number of elements 
that is repeated exactly X times.

Example(s)
[1, 2, 3, 1, 2, 3], 2 == 3
[1, 2, 3, 1, 2, 3], 3 == 0
[1, 3, 3, 5, 5, 5, 5, 5, 3], 3 == 1
 

🔎 EXPLORE
List your assumptions & discoveries:
 

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
function countExactOccurrences(arr, exactOccurrences) {
def countExactOccurrences(arr: list[int], exactOccurrences: int) -> int:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''


def countExactOccurrences(arr: list[int], exactOccurrences: int) -> int:
    _result = 0
    arr_occurrences = {}

    for element in arr:
        frequency_count = arr_occurrences.get(element, 0)+1
        arr_occurrences[element] = frequency_count
        if frequency_count == exactOccurrences:
            _result += 1
        elif frequency_count == exactOccurrences+1:
            _result -= 1

    # for key, value in arr_occurrences.items():
    #     if value == exactOccurrences:
    #         _result += 1
    return _result


print(countExactOccurrences([1, 2, 3, 1, 2, 3], 2) == 3)
print(countExactOccurrences([1, 2, 3, 1, 2, 3], 3) == 0)
print(countExactOccurrences([1, 3, 3, 5, 5, 5, 5, 5, 3], 3) == 1)
arr = [1, 2, 3, 1, 2, 3]
print(countExactOccurrences(arr, 2) == 3)
print(countExactOccurrences(arr, 3) == 0)

arr = [1, 3, 3, 5, 5, 5, 5, 5, 3]
print(countExactOccurrences(arr, 1) == 1)
print(countExactOccurrences(arr, 3) == 1)
print(countExactOccurrences(arr, 5) == 1)

arr = [10, 10, 10, 10]
print(countExactOccurrences(arr, 1) == 0)
print(countExactOccurrences(arr, 3) == 0)
print(countExactOccurrences(arr, 4) == 1)
print(countExactOccurrences(arr, 6) == 0)

arr = [100]
print(countExactOccurrences(arr, 1) == 1)
print(countExactOccurrences(arr, 5) == 0)
print(countExactOccurrences(arr, 100) == 0)
