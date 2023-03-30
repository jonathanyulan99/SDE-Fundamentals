'''
❓ PROMPT
Let's practice recursion by converting functions to and from recursive implementations.
Copy the started code in the language of your choice below, then implement the missing functions and test!

While reading the recursive implementation of *recursiveFactorial* as well as writing *recursiveMax*,
consider the following:

1. What is my base case?
2. Which arguments do I need?
3. What do I do at each recursive step?

Example(s)
iterativeFactorial(3) -> 6
iterativeFactorial(4) -> 24

recursiveMax([4, 2, 7] -> 7
recursiveMax([1, -5, 0] -> 1


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
Javascript Starter Code

function recursiveFactorial(x) {
  if (x <= 1) return 1;
  else return x * recursiveFactorial(x - 1);
}

function iterativeFactorial(x) {
  // TODO: implement
}

function iterativeMax(arr) {
  let result = arr.length > 0 ? arr[0] : null;

  for (let i = 1; i < arr.length; i++) {
    if (arr[i] > result) result = arr[i];
  }

  return result;
}

function recursiveMax(arr, curMax = -Infinity, i = 0) {
  // TODO: implement
  // curMax is an argument that defaults to null if not specified when calling recursiveMax()
  // i is an argument that defaults to 0 if not specified when calling recursiveMax()
  // return null if array is empty
}

Python Starter Code

def recursiveFactorial(x: int) -> int:
  if x <= 1:
    return 1
  return x * recursiveFactorial(x - 1)

def iterativeFactorial(x: int) -> int:
  pass # TODO: implement

def iterativeMax(arr):
  result = arr[0] if len(arr) > 0 else None

  for i in range(1, len(arr)):
    if arr[i] > result:
      result = arr[i]

  return result

def recursiveMax(arr: list[int], curMax=float('-inf'), i = 0) -> int:
  # curMax is an argument that defaults to null if not specified when calling recursiveMax()
  # i is an argument that defaults to 0 if not specified when calling recursiveMax()
  # return null if array is empty
  pass # TODO: implement


🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''


def iterativeFactorial(x: int) -> int:
    _sum = 1
    for num in range(x, 0, -1):
        _sum *= num

    return _sum


print(iterativeFactorial(0))


def solution(arr: list[int]) -> int:
    def helper(arr, curMax, i):
        if len(arr) == i:
            return curMax

        return helper(arr, max(curMax, arr[i]), i+1)
    return helper(arr, float('-inf'), 0)


print(solution([1, 4, 3, 5, 1, 5, 6, 9, 0, -1, -3]))
print(iterativeFactorial(0) == 1)
print(iterativeFactorial(1) == 1)
print(iterativeFactorial(3) == 6)
print(iterativeFactorial(4) == 24)
print(iterativeFactorial(10) == 3628800)

print(solution([4, 2, 7]) == 7)
print(solution([1, -5, 0]) == 1)
print(solution([1, 2, 7]) == 7)
print(solution([1, 0, -5]) == 1)
print(solution([-10, -3, -5]) == -3)
