'''
❓ PROMPT
In a computer, characters are represented as numbers. Each number is assigned to represent a specific character that are recognized world wide through the ASCII 
(see https://en.wikipedia.org/wiki/ASCII) and Unicode (see https://en.wikipedia.org/wiki/Unicode) standards. 
This task is to help you get comfortable manipulating characters by their ASCII or Unicode number values in your language of choice.

In Python, `ord()` takes a character (single character string) and returns it's numeric code. 
The `chr()` function does the inverse, taking a number and returning the corresponding character in a string.

For this task, write a function that takes a string and returns a new string that where each alphabetic character (a-z or A-Z)
is replaced with the character after it. So an 'a' is replaced with 'b', 'b' is replaced with 'c', etc. The 'z' character wraps around to 'a'.

As a follow up, modify the function to take a second parameter which is an increment that can be from 0 (no character shift) or a positive number. 
Shift each alphabetic character that amount (wrapping as before).

To be fair, this question isn't practical. But knowing something about ASCII and Unicode is often useful.

Example(s)
shiftChars("a z") => "b a"
shiftChars("The quick brown fox jumped over the lazy dog.") => "Uif rvjdl cspxo gpy kvnqfe pwfs uif mbaz eph."

🛠️ IMPLEMENT
function shiftChars(s)
def shiftChars(s)

Add a second parameter, k, for the follow up. All return strings.
'''
# ord('char') -> char_unicode_value 
# chr(char_unicode_value) -> char 
def shiftChars(s:str,shift:int=1)->str:
    result = ''
    unicode_lower_value_min = ord('a')
    unicode_lower_value_max = ord('z')
    unicode_upper_value_min = ord('A')
    unicode_upper_value_max = ord('Z')
    
    for char in s:
        if char.isalpha():
            unicode_value = ord(char)
            if char.islower():
                if unicode_value + shift > unicode_lower_value_max:
                    if unicode_value == unicode_lower_value_max: 
                        result += chr(unicode_lower_value_min)
                    else:
                        result+= chr((unicode_value+shift)%26)
                else:
                    result += chr(unicode_value + shift)
            else:
                if unicode_value + shift > unicode_upper_value_max:
                    if unicode_value == unicode_upper_value_max:
                        result += chr(unicode_upper_value_min)
                    else:
                        result += chr((unicode_value + shift)%26)
                else:
                    result += chr(unicode_value + shift)
        else:
            result += char 
    return result 

def get_map(k=1):
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    map = {}
    Acode = ord('A')
    acode = ord('a')
    
    for L in upper:
        l = L.lower()
        Lcode = ord(L)
        offset = (Lcode + k - Acode) % 26
        map[L] = chr(Acode + offset)
        map[l] = chr(acode + offset)
    
    return map

def shift_chars(s, k=1):
    output = []
    the_replacements = get_map(k)
    
    for c in s:
        oc = c
        if the_replacements.get(c) is not None:
            oc = map[c]
        output.append(oc)
    
    return ''.join(output)

print(shiftChars("a") == "b")
print(shiftChars("b") == "c")
print(shiftChars("y") == "z")
print(shiftChars("z")== "a")
print(shiftChars("A") == "B")
print(shiftChars("B") == "C")
print(shiftChars("Y") == "Z")
print(shiftChars("Z") == "A")
print(shiftChars("/") == "/")
print(shiftChars("a", 3) == "d")
print(shiftChars("b", 4) == "f")
print(shiftChars("y", 2) == "a")
print(shiftChars("z", 3)== "c")
print(shiftChars("A", 3) == "D")
print(shiftChars("B", 4) == "F")
print(shiftChars("Y", 2) == "A")
print(shiftChars("Z", 3) == "C")
print(shiftChars("a", 26))# == "a")
print(shiftChars("a", 28) == "c")
print(shiftChars("/", 30) == "/")