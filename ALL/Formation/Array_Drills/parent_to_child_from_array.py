
'''
❓ PROMPT
Given an array of arrays representing relations  *child, parent1, and parent2* in each row, 
print a string representing all children of each parent.

For example: *Ben is the parent of James, Jen*. 
The formatting doesn't matter as long as all children are represented in the final output. 
You will need to return the entire result as strings separated by newlines to match against the strings in these comparisons accurately.

return parentRelationships.join("\n") //javascript
return "\n".join(parentRelationships) #python

Example(s)
Input: []
Output: 'No family relations'

Input: [
  ["James", "Ben", "Lisa"],
  ["George", "Taylor", "Fred"],
  ["Jen", "Ben", "Gloria"]
]
Output:
'Ben is the parent of James, Jen'
'Lisa is the parent of James'
'Taylor is the parent of George'
'Fred is the parent of George'
'Gloria is the parent of Jen'
 

🔎 EXPLORE
List your assumptions & discoveries:
1, A Parent can have multiple children 
2. There can be an empty input 
3. In our Input we can see that Ben had all of his children listed on the first line 
4. We can use a hashmap here 

Insightful & revealing test cases:


🧠 BRAINSTORM
What approaches could work?
Algorithm 1: HashMap with a lst to input the children
Time: O(N) we need to iterate through each row to get the parents and the children of each parent 
Space: O(N)
 

📆 PLAN
Outline of algorithm #: 
- HashMap to assign {parent:[child]}
- iterate through the matrix rows only 
- add the child to the lists of lists of children 
 

🛠️ IMPLEMENT
function parentToChild(relations) {
def parentToChild(relations: list[list[str]]) -> str:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''


def parentToChild(relations: list[list[str]]) -> str:
    if len(relations) == 0 or len(relations[0]) == 0:
        return 'No Family Relations'

    parent_to_children = dict()

    for relation in relations:
        child = relation[0]
        map_to_dict(child, relation[1], parent_to_children)
        map_to_dict(child, relation[2], parent_to_children)

    realtionships = []

    for parent, child in parent_to_children.items():
        realtionships.append(parent + ' is the parent of ' + ''.join(child))

    return '\n'.join(realtionships)


def map_to_dict(child: str, parent: str, dictionary: dict):
    if parent in dictionary:
        dictionary[parent] = dictionary[parent] + [child]
    else:
        dictionary[parent] = [child]


relations = [["James", "Ben", "Lisa"]]
print(parentToChild(relations))  # ==
#       "\
# Ben is the parent of James\n\
# Lisa is the parent of James"
#       )
