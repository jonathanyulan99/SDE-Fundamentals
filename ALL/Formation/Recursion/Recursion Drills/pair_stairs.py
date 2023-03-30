'''
❓ PROMPT
Given a string, compute recursively a new string where identical chars that are adjacent in the original string are separated from each other by a "*".

Example(s)
pairStars("hello") == "hel*lo"
pairStars("xxyy") == "x*xy*y"
pairStars("aaaa") == "a*a*a*a"
 

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
function pairStars(word) {
def pairStars(word: str) -> str:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''


def pairStars(word: str) -> str:
    if len(word) <= 1:
        return word

    if word[0] == word[1]:
        return word[0] + '*' + pairStars(word[1:])

    return word[0]+pairStars(word[1:])


'''


func(aa) ---> a*a 
func(aaaa)---> a*a + a*a 
'''


def pairStars2(word: str, index=0) -> str:
    if index == len(word):
        # this is going to be what is returned at the very end of our recursive calls
        return ""

    sub_string = pairStars2(word, index+1)

    if len(sub_string) > 0 and sub_string[0] == word[index]:
        return word[index] + '*' + sub_string

    return word[index] + sub_string


print(pairStars2("hello"))
'''
""
f(aaaa,2)---> f(aaaa,3) "" word[3] ==> a + "" 
f(aaaa,1)---> f(aaaa,2) a ==> word[2] ===> a + '*' + a
f(aaaa,0)---> f(aaaa,1) a*a ===> a*a*a
f(aaaa,0)----> a*a*a*a 
'''
