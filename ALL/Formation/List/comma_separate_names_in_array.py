'''
❓ PROMPT
Given an array of strings, combine them into one string, comma separated except for the last two pair, 
which should be separated with the word "and". We don't want an Oxford comma, so given ["Sam", "Grant", "Jenny"], 
return "Sam, Grant and Jenny".

Example(s)
commaSeparate(["Daniel", "Craig"]) == "Daniel and Craig"
commaSeparate(["Oliver", "Pixel", "Fido"]) == "Oliver, Pixel and Fido"
 

🔎 EXPLORE
List your assumptions & discoveries:
1. What should be returned if there is only one name or no names? 
2. The minimum amount of names should be 2 or more 
3. We return a string which we need a variable for 
4. Will only be an input of strings 
5. last element if its more than len(list_of_names) is [-1] so we need to place the 'and' between [-2] and [-1]

Insightful & revealing test cases:
1. [] 
2. [one_name] 
3. [name,name,name,....name]

🧠 BRAINSTORM
What approaches could work?
Algorithm 1: We can iterate through the list, and add a comma and every iteration until we get to the last name
at the last name we can add the 'and' and return that string from that sequence of events 
Time: O(N)
Space: O(1)
 

📆 PLAN
Outline of algorithm #: 
1. Declare a string variable to return the result = '' 
2. We need to keep track of the second to last name with 
2.5 We add a comma at every iteration to the string as so result = names[itr] + ','
3. Keep an idea that if its just two names than just add the 'and' and be done 
3. secondary_last_name = len(list) - 2 
4. In our for loop have an 'if' condition that adds that 'and' to the string builder 
 

🛠️ IMPLEMENT
function commaSeparate(names) {
def commaSeparate(names: list[str]) -> str:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''


def commaSeparate(names: list[str]) -> str:
    result = ''
    second_last_name = len(names) - 2
    last_name = len(names) - 1

    if len(names) == 0:
        return

    if len(names) == 1:
        result = names[0]
        return result

    if len(names) == 2:
        result = names[0] + ' and ' + names[1]
        return result

    for x in range(len(names)-1):
        if x == second_last_name:
            result += names[x] + ' and '
        else:
            result += names[x] + ', '

    result += names[last_name]

    return result


print(commaSeparate(["Daniel", "Craig"]))
print(commaSeparate(["Daniel"]))
print(commaSeparate(["Daniel", "Jonathan", "Desiree", "Mike"]))
print(commaSeparate([]))  # []
print(commaSeparate(["Sophie"]))  # "Sophie"
print(commaSeparate(["Daniel", "Craig"]))  # == "Daniel and Craig"
# == "Oliver, Pixel and Fido"
print(commaSeparate(["Oliver", "Pixel", "Fido"]))
# == "Jono, Paavo, Tony and me"
print(commaSeparate(["Jono", "Paavo", "Tony", "me"]))
print(commaSeparate(["John", "John", "John"]))  # == "John, John and John"
print(commaSeparate(["Sean", "John", "Sean"]))  # == "Sean, John and Sean"

'''
# iterative
def commaSeparate(names):
    output = []
    for i in range(len(names)):
        if output:  # need a separator
            if i == len(names) - 1:
                output.append(" and ")
            else:
                output.append(", ")
        output.append(names[i])
    return "".join(output)

# recursive
def commaSeparate(names):
  if not names:
      return ""

  result = ""

  def appendNextVal(index):
    nonlocal result
    if len(names) - index > 0:
      if index == 0:
          result += names[index]
      elif len(names) - index == 1:
          result += ' and ' + names[index]
      else:
          result += ', ' + names[index]

      appendNextVal(index + 1)

  appendNextVal(0)
  return result

'''
