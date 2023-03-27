'''
❓ PROMPT
Given a base-10 integer as a string, parse the integer and return it as an int. 
This problem can be done iteratively and recursively, and it's worth doing both! 

Example(s)
atoi("123") == 123
atoi("4") == 4
atoi("007") == 7
atoi("-1") == -1
 

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
function atoi(intAsString) {
def atoi(intAsString: str) -> int:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
# atoi("123") == 123
# atoi("4") == 4
# atoi("007") == 7
# atoi("-1") == -1


# def atoi(string: str) -> int:
#     def helper(string, level):
#         if len(string) <= 1:
#             return int(string) * 10 ** level

#         return  * helper(string[1:], level-1)

#     return helper(string, len(string)-1)


def atoi_recursive(intAsString: str) -> int:
    charMap = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    }

    def recursiveHelper(intAsString, index, value=0):
        if index == len(intAsString):
            return value

        nextValue = value * 10 + charMap[intAsString[index]]
        return recursiveHelper(intAsString, index + 1, nextValue)

    negative = intAsString[0] == '-'
    start = 1 if negative else 0

    value = recursiveHelper(intAsString, start)
    return -value if negative else value


print(atoi_recursive('3'))


def atoi_iterative(intAsString: str) -> int:
    charMap = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    }
    value = 0
    negative = intAsString[0] == '-'
    start = 1 if negative else 0
    for i in range(start, len(intAsString)):
        digit = charMap[intAsString[i]]
        value = value * 10 + digit
    return -value if negative else value


print(atoi_iterative("-1000"))
