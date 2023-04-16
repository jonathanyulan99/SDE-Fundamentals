'''
❓ PROMPT
You will be implementing a function called stringify which will take in a Javascript Object
and return the JSON representation of the object as a string. 
This function is actually built into Javascript as `JSON.stringify(object)` but you have to write yours from scratch!

You may want to take a moment to review the rules for [JSON syntax](https://www.w3schools.com/js/js_json_syntax.asp).

Example(s)
{x: 5, y: "Oliver"}
 

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
function stringify(obj) {
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

JSON RULES:
    Data is in name/value pairs
    Data is separated by commas
    Curly braces hold objects
    Square brackets hold arrays
    
obj = {name: "John", age: 30, city: "New York"}

'''
# stringify(takes in any obj) --> converts it into a string 
def stringify(obj:object)->str:
    # check for validity of the object
    if not obj:
        return None 
    
    # we can use isinstance(obj,type) to return values appropriately 
    # we can return the values using the f'' string syntax 
    if isinstance(obj,str):
        # if we only use one pair of outside quotes than we will not be able to see the string surroudned in "" quotes 
        # we can also use the \escape character here 
        # return f'"{obj}"'
        # return f"\"{obj}\""
        # escape character goes before the character we are trying to ignore in our return/print 
        return f"\"{obj}\""
    
    # we can check for numbers by checking for isinstance(num,int) or isinstance(num,float)
    # the key part of this function is to return the string version of what the object we are passing is thus...
    if isinstance(obj,int) or isinstance(obj,float):
        return f'{str(obj)}'
    
    # check for the type of list of elements we are inputting 
    if isinstance(obj,list):
        # break our list into elements 
        # we can call our stringify() function on each element in our list 
        list_elements = [stringify(val) for val in obj]
        # when we return we want to return a list of values that are separated by the a ,_ 
        # remember the list elements is a list of seperate strings 
        # need to join to return one list 
        # what is in the curly braces is what is going to get returned surrounded by []
        return f"[{', '.join(list_elements)}]"
    
    # for dictionary values being inputted 
    dict_elements = [] 
    for key in obj:
        if obj.get(key,-1) != -1:
            dict_elements.append(f'\"{key}\":{stringify(obj[key])}')
            print(dict_elements)
    return f'{{{", ".join(dict_elements)}}}'
    

obj = {
  'x': 5,
  'y': -8,
  'nested': {
    'z': "this is a string"
  }
}
print(stringify(obj),type(stringify(obj)))