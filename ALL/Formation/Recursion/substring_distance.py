'''
❓ PROMPT
Given a string and a non-empty substring *sub*, compute recursively the size of the 
largest substring which starts and ends with the given *sub* string and return its length, 
including the length of the substrings. When *sub* is multiple characters, they may overlap 
with each other and share characters.

Example(s)
strDist("catcowcat", "cat") == 9
strDist("catcowcat", "cow") == 3
strDist("cccatcowcatxx", "cat") == 9
strDist("ooowhwhwooo", "whw") == 5
 

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
function strDist(word, sub) {
def strDist(word: str,  sub: str) -> int:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
# strDist("catcowcat", "cat") == 9
# strDist("catcowcat", "cow") == 3
# strDist("cccatcowcatxx", "cat") == 9
# strDist("ooowhwhwooo", "whw") == 5


def strDist(word: str,  sub: str) -> int:
    def str_dist_helper(word, sub, start, end):
        if len(word) < len(sub):
            return 0
        if word[start:len(sub)] == sub and word[end-len(sub):] == sub:
            return len(sub)

        if not word[start:len(sub)] == sub:
            return str_dist_helper(word[start], sub, start+1, end)

        return str_dist_helper(word[0:end], sub, start, end-1)
    return str_dist_helper(word, sub, 0, len(word)-1)


print(strDist("cccatcowcatxx", "cat"))


def strDist(word: str,  sub: str) -> int:
    if len(word) < len(sub):
        return 0  # base case when the word is smaller than "sub"

    if word[0:len(sub)] == sub and word[len(word) - len(sub):] == sub:
        return len(word)  # base case when the word starts and ends with "sub"

    if not word[0:len(sub)] == sub:
        return strDist(word[1:], sub)  # remove the first character

    return strDist(word[0:len(word) - 1], sub)  # remove the last character


print(strDist("catcowcat", "cat"))
