'''
❓ PROMPT
In a computer, characters are represented as numbers. Each number is assigned to represent a specific character that are recognized world wide through the ASCII ( see https://en.wikipedia.org/wiki/ASCII) and Unicode (see https://en.wikipedia.org/wiki/Unicode) standards. This task is to help you get comfortable manipulating characters by their ASCII or Unicode number values in your language of choice.

In Python, `ord()` takes a character (single character string) and returns it's numeric code. The `chr()` function does the inverse, taking a number and returning the corresponding character in a string.

In Javascript, `'c'.charCodeAt()` returns the numeric code for 'c'. Use `String.fromCharCode(42)` for the inverse, in this case returning a string with the character corresponding to the number 42.

For this task, write a function that takes a string and returns a new string that where each alphabetic character (a-z or A-Z) is replaced with the character after it. So an 'a' is replaced with 'b', 'b' is replaced with 'c', etc. The 'z' character wraps around to 'a'.

As a follow up, modify the function to take a second parameter which is an increment that can be from 0 (no character shift) or a positive number. Shift each alphabetic character that amount (wrapping as before).

To be fair, this question isn't practical. But knowing something about ASCII and Unicode is often useful.

Example(s)
shiftChars("a z") => "b a"
shiftChars("The quick brown fox jumped over the lazy dog.") => "Uif rvjdl cspxo gpy kvnqfe pwfs uif mbaz eph."

 

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
function shiftChars(s)
def shiftChars(s)

Add a second parameter, k, for the follow up. All return strings.
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''