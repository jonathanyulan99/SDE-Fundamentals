'''
❓ PROMPT
In mathematics, the factorial of a non-negative integer N, denoted as N! 
It is the multiplication product of all positive integers <= N. Compute the result recursively (without loops).

Example(s)
factorial(3) == 6
factorial(5) == 120
 

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
function factorial(n) {
def factorial(n: int) -> int:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
# let us try to do this tail-up recursion wise
# change our header to include 1 to default at one
# 0! = 1
# [0,+infinity)


def factorial(n: int, sum=1) -> int:
    if n == 0 or n == 1:
        return sum

    # returned only the tail end of recursive sum
    return factorial(n-1, sum*n)


print(factorial(5))
print(factorial(12) == 479001600)
print(factorial(10) == 3628800)
print(factorial(5) == 120)
print(factorial(3) == 6)
print(factorial(2) == 2)
print(factorial(1) == 1)
