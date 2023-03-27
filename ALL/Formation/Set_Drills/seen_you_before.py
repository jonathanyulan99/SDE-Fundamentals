'''
You're the shift manager at a new ice cream store opening. To ensure everyone 
gets a chance to taste the new flavors, there is a limit of one serving per person.

You notice that people are not following this rule and are coming back into the line
to get another serving of ice cream.

Given an array of people's names, return True if you come across a person you've already
seen in line. Otherwise, False.

Can you think of any data structures that might help?
 

EXAMPLE(S)
A line with people ['Pixel', 'Pinky', 'Oliver'] should return False, as there are no people coming back.
A line with people ['Neko', 'Moose', 'Neko'] should return True, since Neko decided to come back.
 

FUNCTION SIGNATURE
def seenYouBefore(patrons: list) -> bool:
'''


def seenYouBefore(patrons: list) -> bool:
    patron_set = set()

    for patron in patrons:
        if patron in patron_set:
            return True
        else:
            patron_set.add(patron)

    return False


print(seenYouBefore([]) == False)
print(seenYouBefore(['Sweet Tea', 'Oliver', 'Pinky',
      'Sweet Tea', 'Pixel', 'Jelly']) == True)
print(seenYouBefore(['Neko', 'Neko']) == True)
print(seenYouBefore(['Moose', 'Porkchop', 'Sweet Tea', 'Hercules']) == False)
