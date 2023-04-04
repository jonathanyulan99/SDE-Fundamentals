'''
❓ PROMPT
Because strings are immutable, this problem takes more work than it does for an array.
With an array, we can move individual values around and assign them into different
locations. But with a string, we need to actually create an entirely new one.

Yes, in many modern languages this can be done with built in methods, 
but here we're working on basic coding patterns and coding fluency. 
We're going to mostly write this out.

Example(s)
reverseString("noitamroF") => "Formation"
 

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
function reverseString(s)
def reverseString(s):
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''


def reverseString(s):
    s = list(s)
    # unpacking below example
    # s = [*s]
    # or
    # s = [0] * len(s)
    beg = 0
    end = len(s)-1

    while beg < end:
        s[beg], s[end] = s[end], s[beg]
        beg += 1
        end -= 1

    return ''.join(s)


print(reverseString('noitamroF'))
print(reverseString("") == "")
print(reverseString("a") == "a")
print(reverseString("foo") == "oof")
print(reverseString("food") == "doof")
