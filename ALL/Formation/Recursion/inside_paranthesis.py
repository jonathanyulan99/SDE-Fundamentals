'''
❓ PROMPT
Given a string that contains exactly 1 pair of parentheses,
compute recursively a new string made of only the parentheses and their contents, so "xyz(abc)123" yields "(abc)".

Example(s)
parenBit("xyz(abc)123") == "(abc)"
parenBit("x(hello)") == "(hello)"
parenBit("(xy)1") == "(xy)"


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
function parenBit(word) {
def parenBit(word: str) -> str:


🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''


def parenBit(word: str) -> str:
    if word[-1] == ')' and word[0] == "(":
        return word

    if word[0] != '(':
        return parenBit(word[1:])

    if word[len(word)-1] != ')':
        return parenBit(word[:-1])


print(parenBit("xyz(abc)123") == "(abc)")
print(parenBit("x(hello)") == "(hello)")
print(parenBit("(xy)1") == "(xy)")
print(parenBit("not really (possible)") == "(possible)")
print(parenBit("(abc)") == "(abc)")
print(parenBit("(abc)xyz") == "(abc)")
print(parenBit("(abc)x") == "(abc)")
print(parenBit("(x)") == "(x)")
print(parenBit("()") == "()")
print(parenBit("res (ipsa) loquitor") == "(ipsa)")
print(parenBit("hello(not really)there") == "(not really)")
print(parenBit("ab(ab)ab") == "(ab)")
print(parenBit("ab(ab)ab") == "(ab)")
