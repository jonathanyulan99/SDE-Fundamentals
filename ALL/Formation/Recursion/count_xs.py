'''
❓ PROMPT
Given a string, compute recursively (no loops) the number of lowercase 'x' chars in the string.

Example(s)
countX("xxhixx") == 4
countX("xhixhix") == 3
countX("hi") == 0
 

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
function countX(word) {
def countX(word: str) -> int:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
# xxhixx
# xhixx
# hixx
# ixx
# xx
# x


def countX(word: str) -> int:
    if len(word) == 0:
        return 0
    sum = 0
    sum = countX(word[1:])
    # if you wanted to check for capital X's then just a simple or condition at word[0] == 'X'
    if word[0] == 'x':
        sum += 1

    return sum


print(countX("xxhixx"))  # 4
print(countX("xhixhix"))  # 3
print(countX("hi"))  # 0
print(countX("xxhixx") == 4)
print(countX("xhixhix") == 3)
print(countX("hiX") == 0)
print(countX("XXXhXXX") == 0)
print(countX("x") == 1)
print(countX("") == 0)
print(countX("hihi") == 0)
print(countX("hiAAhi12hi") == 0)
