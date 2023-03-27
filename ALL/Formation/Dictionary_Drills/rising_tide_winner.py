'''
❓ PROMPT
Given an array of Fellows representing nominations for a Rising Tide Award at Formation, 
return the name of the winning Fellow with the most number of nominations

Example(s)
risingTideWinner(["oliver", "pixel", "pinky", "pixel"]) == "pixel"
 

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
function risingTideWinner(nominations) {
def risingTideWinner(nominations: list[str]) -> str:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''


def risingTideWinner(nominations: list[str]) -> str:
    if not nominations:
        return None

    winner = nominations[0]
    dict_people_counts = dict()
    max_counts = 0

    for index, name in enumerate(nominations):
        counts = dict_people_counts.get(name, 1)

        if name not in dict_people_counts:
            dict_people_counts[name] = 1
        elif name in dict_people_counts:
            dict_people_counts[name] += 1
        if index >= 1 and counts >= max_counts:
            winner = sorted(list([name, winner]))[1]
        max_counts = counts

    return winner


print(risingTideWinner([]) == None)
print(risingTideWinner(["pinky"]) == "pinky")
print(risingTideWinner(["tony", "zoe", "jess", "jono", "paavo"]) == "zoe")
print(risingTideWinner(["oliver", "pixel", "pinky", "pixel"]) == "pixel")
print(risingTideWinner(
    ["oliver", "pixel", "pinky", "pixel", "pinky"]) == "pixel")
print(risingTideWinner(
    ["oliver", "pixel", "pinky", "pinky", "pixel"]) == "pixel")
