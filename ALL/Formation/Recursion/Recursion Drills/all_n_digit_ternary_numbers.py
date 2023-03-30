
'''
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
function generateNDigitTernaries(n) {
def generateNDigitTernaries(n: int) -> list[str]:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

❓ PROMPT
The decimal system uses the digits 0-9, the binary system uses the digits 0 and 1,
and the hexadecimal system uses the digits 0-9 and the letters A-F.  
The ternary system is a base-3 numeral system that uses the digits 0, 1, and 2.

Given a number *n*, write a function that prints out all *n*-digit ternary numbers.

Example(s)
Numbers starting with zero shouldn't normally be included but the ternary representing 
the zero value is a valid 1-digit ternary. No other strings should start with a "0"!

generateNDigitTernaries(1) == ["0","1","2"]
generateNDigitTernaries(2) == ["10","11","12","20","21","22"]

For each index, loop through all the ternary digits to build a permutation with 0, 1, or 2 at that index. 
Then recursively calling your function. There is a loop in each recursive call so every digit will be used at every index. 
This should continue until the base case is met; which is when the length of the string equals N.
Finally, when the recursive call unwinds and returns back inside the loop, un-append the digit so that the next loop iteration 
will replace that index by appending the next ternary digit.
There's a special case for n=1 to include "0" in the output.

'''


def generateNDigitTernaries(n: int) -> list[str]:
    result = []
    s = []

    def helper():
        if len(s) == n:
            # using this to not make a new string every time
            # not using a non local
            result.append(''.join(s))
            return

        for i in range(3):
            s.append(str(i))
            helper()
            s.pop()

    if n == 1:
        result.append('0')

    for i in range(1, 3):
        result.append(str(i))
        helper()
        s.pop()

    return result
