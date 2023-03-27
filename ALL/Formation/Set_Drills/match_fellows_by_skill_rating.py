'''
❓ PROMPT
Given an input dictionary mapping Fellows (as string names) to skill ratings,
return true if you're able to pair up Fellows with matching skill ratings with no Fellows leftover.

Example(s)
skillMap = {"oliver": 3, "pixel": 3, "pinky": 5, "tobey": 5}
canMatchFellows(skillMap) == True

skillMap = {"oliver": 3, "pixel": 4, "pinky": 5, "tobey": 5}
canMatchFellows(skillMap) == False
 

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
function canMatchFellows(skillMap) {
def canMatchFellows(skillMap: dict) -> bool:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.


skillMap = {"oliver": 3, "pixel": 3, "pinky": 5, "tobey": 5}
canMatchFellows(skillMap) == True

skillMap = {"oliver": 3, "pixel": 4, "pinky": 5, "tobey": 5}
canMatchFellows(skillMap) == False
'''


def canMatchFellows(skillMap: dict) -> bool:
    if not skillMap:
        return True

    skill_dict = {}
    for key, values in skillMap.items():
        if values not in skill_dict:
            skill_dict[values] = 1
        else:
            skill_dict[values] += 1

    for values in skill_dict.values():
        if values < 2:
            return False
        elif values % 2 != 0:
            return False

    return True


skillMap = {"oliver": 3, "pixel": 3, "pinky": 5, "tobey": 5}
print(canMatchFellows(skillMap) == True)

skillMap = {"oliver": 3, "pixel": 3, "pinky": 5, "tobey": 5}
print(canMatchFellows(skillMap) == True)

skillMap = {"oliver": 3, "pixel": 4, "pinky": 5, "tobey": 5}
print(canMatchFellows(skillMap) == False)

skillMap = {"oliver": 3, "pixel": 3, "pinky": 3}
print(canMatchFellows(skillMap) == False)

skillMap = {"oliver": 3, "pixel": 3, "pinky": 5, "tobey": 5, "paavo": 1}
print(canMatchFellows(skillMap) == False)

skillMap = {"oliver": 3, "pixel": 3, "pinky": 3, "tobey": 3}
print(canMatchFellows(skillMap) == True)

print(canMatchFellows({"oliver": 1}) == False)

print(canMatchFellows({}) == True)


def can_match_fellows(skillMap: dict) -> bool:
    skill_set = set()
    if skillMap is None:
        return True

    for k, v in skillMap.items():
        if v in skill_set:
            skill_set.remove(v)
        else:
            skill_set.add(v)

    if len(skill_set) == 0:
        return True
    else:
        return False


skillMap = {"oliver": 3, "pixel": 3, "pinky": 5, "tobey": 5}
print(can_match_fellows(skillMap) == True)

skillMap = {"oliver": 3, "pixel": 3, "pinky": 5, "tobey": 5}
print(can_match_fellows(skillMap) == True)

skillMap = {"oliver": 3, "pixel": 4, "pinky": 5, "tobey": 5}
print(can_match_fellows(skillMap) == False)

skillMap = {"oliver": 3, "pixel": 3, "pinky": 3}
print(can_match_fellows(skillMap) == False)

skillMap = {"oliver": 3, "pixel": 3, "pinky": 5, "tobey": 5, "paavo": 1}
print(can_match_fellows(skillMap) == False)

skillMap = {"oliver": 3, "pixel": 3, "pinky": 3, "tobey": 3}
print(can_match_fellows(skillMap) == True)

print(can_match_fellows({"oliver": 1}) == False)

print(can_match_fellows({}) == True)
