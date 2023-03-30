'''
❓ PROMPT
Given a string, compute recursively (no loops) a new string where all appearances of "pi" have been replaced by "3.14".

Example(s)
changePi("xpix") == "x3.14x"
changePi("pipi") == "3.143.14"
changePi("pip") == "3.14p"
 

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
function changePi(word) {
def changePi(word: str) -> str:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.



'''


def changePi(word: str) -> str:
    if len(word) <= 1:
        return word

    if word[0] == 'p' and word[1] == 'i':
        return '3.14' + changePi(word[2:])

    return str(word[0]) + changePi(word[1:])


print(changePi("xpix") == "x3.14x")
print(changePi("pipi") == "3.143.14")
print(changePi("pip") == "3.14p")
print(changePi("pi") == "3.14")
print(changePi("hip") == "hip")
print(changePi("p") == "p")
print(changePi("x") == "x")
print(changePi("") == "")
print(changePi("pixx") == "3.14xx")
print(changePi("xyzzy") == "xyzzy")

'''

("pip") == 3.14 return changePi(word[2:])
changePi("pip") == "3.14p"
changePi("xpix") == "x3.14x"
changePi("pipi") == "3.143.14"
'''
