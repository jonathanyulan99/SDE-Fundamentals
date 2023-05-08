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
def atoi(intAsString: str) -> int:
    str_to_num_dict = {
        '0': 0, '1':1, '2':2, '3':3 , '4':4, '5':5, '6':6, '7':7, '8':8, '9':9
    }
    
    is_negative = intAsString[0] == '-'
    if is_negative:
        intAsString = intAsString[1:]
        
    def helper(num,end,power): 
        if end < 0: 
            return 0
        
        digit = str_to_num_dict[num[end]] 
        digit *= (10 ** power)
        return digit + helper(num,end-1,power+1)
         
    
    integer = helper(intAsString,len(intAsString)-1,0)
    return integer if not is_negative else -1 * integer 

print(atoi("123") == 123)
print(atoi("4") == 4)
print(atoi("0") == 0)
print(atoi("007") == 7)
print(atoi("-1") == -1)
print(atoi("-234") == -234)
print(atoi("600") == 600)
print(atoi("00500") == 500)

def atoi_recursive(intAsString: str) -> int:
    charMap = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
    '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,}
    def recursiveHelper(intAsString, index, value = 0):
        if index == len(intAsString):
            return value

        nextValue = value * 10 + charMap[intAsString[index]]
        return recursiveHelper(intAsString, index + 1, nextValue)

    negative = intAsString[0] == '-'
    start = 1 if negative else 0

    value = recursiveHelper(intAsString, start)
    return -value if negative else value

print(atoi_recursive("123") == 123)
print(atoi_recursive("4") == 4)
print(atoi_recursive("0") == 0)
print(atoi_recursive("007") == 7)
print(atoi_recursive("-1") == -1)
print(atoi_recursive("-234") == -234)
print(atoi_recursive("600") == 600)
print(atoi_recursive("00500") == 500)