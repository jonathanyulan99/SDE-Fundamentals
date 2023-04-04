'''
❓ PROMPT
You're a bartender and have to look out for your patrons - you don't want them 
to drink too much. Assume everyone has the same drink, and everyone has the same 
set amount of "allowed servings".

Given an array of patrons (denoted by their names, eg: Adrian) and an integer value
representing "allowed servings", return True if someone attempts to go over the allowed
number of servings per person.

Otherwise, False if no one drinks too much.

Can you think of any data structures that might help?

Example(s)
patrons = ['Joe', 'Bart', 'Larry', 'Joe', 'Carl', 'Doug', 'Joe']
allowedServings = 2

returns True because Joe went over the limit.
 

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
function limitedServings(patrons, allowedServings) {
def limitedServings(patrons: list[str], allowedServings: int) -> bool:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''


def limitedServings(patrons: list[str], allowedServings: int) -> bool:
    patron_drink_occurrences = {}

    for patron in patrons:
        patron_value = patron_drink_occurrences.get(patron, 0)+1
        if patron_value > allowedServings:
            return True
        patron_drink_occurrences[patron] = patron_value

    return False


patrons = ['Joe', 'Bart', 'Larry', 'Joe',
           'Carl', 'Doug', 'Bart', 'Larry', 'Bart']
allowedServings = 2
print(limitedServings(patrons, allowedServings))
print(limitedServings([], 3) == False)
print(limitedServings(['Joe', 'Bart', 'Larry',
      'Joe', 'Carl', 'Doug', 'Joe'], 2) == True)
print(limitedServings(['Joe', 'Joe'], 3) == False)
print(limitedServings(['Joe', 'Joe', 'Adrian', 'Adrian'], 3) == False)
print(limitedServings(['Adrian', 'Bart', 'Carl', 'Doug'], 1) == False)
print(limitedServings(['Adrian', 'Bart', 'Carl'], 0) == True)
