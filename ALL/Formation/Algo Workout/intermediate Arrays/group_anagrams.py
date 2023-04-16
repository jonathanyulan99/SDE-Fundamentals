
'''
❓ PROMPT
Given an array of strings, group all anagrams together in an array and return an array of these groups.

Example(s)
Input: ["bat", "cat", tab, "car", "atb"]
Output: [["bat", "tab, "atb"], ["cat"], ["car"]]
 

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
func groupAnagrams(input: [String]) => [[String]]:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.
Input: ["bat", "cat", tab, "car", "atb"]
Output: [["bat", "tab, "atb"], ["cat"], ["car"]]
# bat 
# sorted(bat) --> atb 
# d[atb] = [bat]
'''
def group_anagrams(input: list[str])->list[list[str]]:
    d = {} 
    for index in range(len(input)):
        word_sorted = ''.join(sorted(input[index]))
        value = d.get(word_sorted,'X')
        if value == 'X':
            d[word_sorted] = [input[index]]
        else:
            d[word_sorted].append(input[index])

    return list(d.values()) 

print(group_anagrams(["bat", "cat", 'tab', "car", "atb"]))