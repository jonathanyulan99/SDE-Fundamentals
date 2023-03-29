'''❓ PROMPT
Many teams use a type of tool called a linter to scan code to ensure it follows certain 
standards and best practices. One common rule a linter might check for is the depth of nesting 
of control flow. Functions with many levels of nesting are often overly complex, hard to read or 
modify, and can be bug farms. We're going to write a function to determine the depth of control flow 
for if-statements so that teams will be automatically notified if it gets too deep.

In Visual Basic (an old language I hope most of you never need to use), if statements are bounded by 
four keywords: if, elseif, else, and endif. Given a sequence of these keywords, return the max nesting 
depth or -1 if the structure is incorrect.

The structure is incorrect when:
1. The first keyword is anything other than an if.
2. If and endif keywords do not pair up or are out of order.
3. An else or elseif is not inside an if.
4. There are two else blocks in a row.
5. An elseif follows an else at a given level.

Start by implementing this with only if, and endif. Then add support for else. 
Once that is working, modify the code to support elseif as well.

Example(s)
vbNesting(["if"]) == -1
vbNesting(["endif"]) ==  -1
vbNesting(["if", "endif"]) == 1
vbNesting(["if", "else", "endif"]) == 1
vbNesting(["if", "endif", "if", "endif"]) == 1
vbNesting(["if", "if", "endif", "endif"]) == 2
vbNesting(["if", "if", "if", "endif", "endif", "endif"]) == 3
vbNesting(["if", "if", "if", "endif", "endif", "if", "endif", "endif"]) == 3
 

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
function vbNesting(controlFlow) {
def vbNesting(controlFlow: list[str]) -> int:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

Example(s)
vbNesting(["if"]) == -1
vbNesting(["endif"]) ==  -1
vbNesting(["if", "endif"]) == 1
vbNesting(["if", "else", "endif"]) == 1
vbNesting(["if", "endif", "if", "endif"]) == 1
vbNesting(["if", "if", "endif", "endif"]) == 2
vbNesting(["if", "if", "if", "endif", "endif", "endif"]) == 3
vbNesting(["if", "if", "if", "endif", "endif", "if", "endif", "endif"]) == 3

The structure is incorrect when:
1. The first keyword is anything other than an if.
2. If and endif keywords do not pair up or are out of order.
3. An else or elseif is not inside an if.
4. There are two else blocks in a row.
5. An elseif follows an else at a given level.

Keep a stack of keywords (initialize to empty), a variable tracking the max depth (initialize to 0).
Iterate through the list of keywords:
Push an if on the stack and check to see if this is a new max depth
Pop from the stack on an endif (or return "Invalid" if there is nothing to pop)
For an else, pop the current stop of the stack. If that keyword is an if, push the else. 
If it's an else, return invalid.
At the end return the max depth if the stack is empty and "Invalid" otherwise.
'''


def vbNesting(controlFlow: list[str]) -> int:
    stack = []
    _depth = 0

    for ele in controlFlow:
        if ele == 'if':
            stack.append(ele)
            if len(stack) > _depth:
                _depth = len(stack)
        elif ele == 'endif':
            if len(stack) == 0:
                return -1
            else:
                popped = stack.pop()
        elif ele == 'elseif' or ele == 'else':
            if len(stack) == 0:
                return -1
            popped = stack.pop()
            if popped == 'if' or popped == 'elseif':
                stack.append(ele)
            else:
                return -1

    return _depth if len(stack) == 0 else -1


print(vbNesting(["if", "if", "if", "endif",
      "endif", "if", "endif", "endif"]) == 3)

print(vbNesting(["if"]) == -1)
print(vbNesting(["endif"]) == -1)
print(vbNesting(["if", "endif"]) == 1)
print(vbNesting(["if", "if", "if", "endif", "endif", "endif"]) == 3)
print(vbNesting(["if", "if", "if", "endif",
      "endif", "if", "endif", "endif"]) == 3)
print(vbNesting(["if", "else", "endif"]) == 1)
print(vbNesting(["if", "endif", "if", "endif"]) == 1)
print(vbNesting(["if", "if", "endif", "endif"]) == 2)
print(vbNesting(["else"]) == -1)
print(vbNesting(["endif", "if"]) == -1)
print(vbNesting(["if", "else", "if", "endif", "endif"]) == 2)
print(vbNesting(["if", "endif", "if", "elseif",
      "else", "endif", "endif"]) == -1)
print(vbNesting(["if", "elseif", "elseif", "elseif", "endif"]) == 1)
print(vbNesting(["if", "elseif", "else", "endif"]) == 1)
print(vbNesting(["if", "if", "elseif", "else", "endif", "endif"]) == 2)
print(vbNesting(["if", "endif", "if", "elseif", "else", "endif"]) == 1)
print(vbNesting(["if", "else", "elseif", "endif"]) == -1)
print(vbNesting(["if", "else", "else", "endif"]) == -1)
