'''
❓ PROMPT
We have bunnies standing in a line, numbered 1, 2, ... The odd bunnies (1, 3, ..) 
have the usual 2 ears. The even bunnies (2, 4, ..) we'll say have 3 ears because they each have a raised foot. 
Recursively return the number of "ears" in the bunny line 1, 2, ... n (without loops or multiplication).

Example(s)
bunnyEarsTwist(2) == 5
bunnyEarsTwist(3) == 7
bunnyEarsTwist(5) == 12
 

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
function bunnyEarsTwist(bunnies) {
def bunnyEarsTwist(bunnies: int) -> int:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

# odd bunnies have 2 ears
# even bunnies have 3 
bunny(2) ... 2 = 3 ears
bunny(1) ... 1 = 2 ears
bunny(0) ... return 
return 5 
'''


def bunnyEarsTwist(bunnies: int) -> int:
    if bunnies < 1:
        return 0

    if bunnies % 2 == 0:
        # even
        return 3 + bunnyEarsTwist(bunnies-1)
    else:
        return 2 + bunnyEarsTwist(bunnies-1)


print(bunnyEarsTwist(5))
print(bunnyEarsTwist(12) == 30)
print(bunnyEarsTwist(10) == 25)
print(bunnyEarsTwist(5) == 12)
print(bunnyEarsTwist(3) == 7)
print(bunnyEarsTwist(2) == 5)
print(bunnyEarsTwist(1) == 2)
print(bunnyEarsTwist(0) == 0)

'''
func(1)----> return 1 + 0
func(2)---->return 3 + bunnyEarsTwist(1) == 1 
func(3)---> return 2 + bunnyEarsTwist(2) == 6
func(4)--->return 3 + bunnyEarsTwist(3) == 9 
func(5)--->return 2 + bunnyEarsTwist(4) == 11
func(6)--->return 3 + bunnyEarsTwist(5) == 14
'''
