'''
❓ PROMPT
Given a non-negative int n, return the sum of its digits recursively (no loops).
Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the
rightmost digit (126 / 10 is 12).

Example(s)
sumDigits(12) == 3
sumDigits(49) == 13
sumDigits(126) == 9


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
function sumDigits(n) {
def sumDigits(n: int) -> int:


🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''


def sumDigits(n: int) -> int:
    def helper(n):
        if n <= 0:
            return 0

        prev = helper(n//10)
        prev += n % 10
        return prev

    return helper(n)


print(sumDigits(126))
print(sumDigits(126) == 9)
print(sumDigits(49) == 13)
print(sumDigits(12) == 3)
print(sumDigits(10) == 1)
print(sumDigits(1) == 1)
print(sumDigits(0) == 0)
print(sumDigits(730) == 10)
print(sumDigits(1111) == 4)
print(sumDigits(11111) == 5)
print(sumDigits(10110) == 3)
print(sumDigits(235) == 10)

'''

f(0,0)---->return 0 
f2(1,0)---->f2(1//0,0) ---> 0 1%10 == 1 
f2(12,0)---> f2(12//10,0)---->1 + 
f(12) ---> f2(12,0)
'''
