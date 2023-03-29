'''
❓ PROMPT
Given a string, insert a star (*) between each character.

Example(s)
addStars("hello") == "h*e*l*l*o"
addStars("abc") == "a*b*c"
addStars("ab") == "a*b"
 

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
function addStars(word) {
def addStars(word: str) -> str:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.
addStars("hello") == "h*e*l*l*o"
addStars("abc") == "a*b*c"
addStars("ab") == "a*b"
'''


def addStars(word: str) -> str:
    if len(word) < 2:
        return word

    return word[0] + '*' + addStars(word[1:])


'''
return word ==> o
return 'l' + '*' + addStars('o') <== o
return 'l' + '*' + addStars('lo') <== l*o
return 'e' + '*' + addStars('llo') <== e*l*l*o
return 'h' + '*' + addStars('ello') <== h*e*l*l*o
addStars('hello')
'''
print(addStars("hello") == "h*e*l*l*o")
print(addStars("abc") == "a*b*c")
print(addStars("ab") == "a*b")
print(addStars("a") == "a")
print(addStars("") == "")
print(addStars("3.14") == "3*.*1*4")
print(addStars("Chocolate") == "C*h*o*c*o*l*a*t*e")
print(addStars("1234") == "1*2*3*4")
