
'''
❓ PROMPT
Given an input dictionary mapping from the name of Fellows to their numerical skill rating, 
return the skill rating with the highest number of Fellows.

Example(s)
{"oliver": 3, "pixel": 1, "pinky": 3} => 3
 

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
function highestSkillOverlap(fellowSkills) {
def highestSkillOverlap(fellowSkills: dict) -> int:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

import random


def highestSkillOverlap(fellowSkills: dict) -> int:
    # check for empty dict
    if not fellowSkills:
        return None

    skill_dictionary = dict()
    max_skill = -10000000000
    max_frequency = 0
    container = list()

    for k, v in fellowSkills.items():
        skill_level = fellowSkills.get(k)

        if skill_level in skill_dictionary:
            skill_dictionary[v] += 1
        elif skill_level not in skill_dictionary:
            skill_dictionary[v] = 1

        frequency = skill_dictionary[v]

        if frequency >= max_frequency:
            max_frequency = frequency
            container.append(v)
            max_skill = v

    if len(container) > 1:
        random_value = random.randrange(0, len(container))
        return container[random_value]

    return max_skill


print(highestSkillOverlap(dict()) == None)

fellowSkills = {"oliver": 3}
print(highestSkillOverlap(fellowSkills) == 3)

fellowSkills = {"oliver": 3, "tobey": 3}
print(highestSkillOverlap(fellowSkills) == 3)

fellowSkills = {"oliver": 3, "pinky": 4, "pixel": 2, "tobey": 1}
print(1 <= highestSkillOverlap(fellowSkills) <= 4)
print(highestSkillOverlap(fellowSkills))

fellowSkills = {"oliver": 3, "pinky": 1, "pixel": 2, "tobey": 1}
print(highestSkillOverlap(fellowSkills) == 1)

fellowSkills = {"tony": 3, "jess": 1, "paavo": 2,
                "zoe": 1, "jono": 2, "angus": 3}
print(1 <= highestSkillOverlap(fellowSkills) <= 3)
