'''
❓ PROMPT
Given a string and a non-empty substring *sub*, compute recursively if at least n copies of sub appear in the string somewhere, possibly with overlapping. N will be non-negative.

Example(s)
strCopies("catcowcat", "cat", 2) == True
strCopies("catcowcat", "cow", 2) == False
strCopies("catcowcat", "cow", 1) == True
 

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
function strCopies(word, sub, n) {
def strCopies(word: str, sub: str, n: int) -> bool: 
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

# abcdef
# cde 
def strCopies(word: str, sub: str, n: int) -> bool:
        # one-liner
        # return True if n == word.count(sub) else False 
        def helper(word,sub,start,end):
            if len(word) < start + len(sub):
                return 0 
        
            if word[start:end] == sub: return 1 + helper(word,sub,start+1,end+1)
            return helper(word,sub,start+1,end+1)
            
        count = helper(word,sub,0,len(sub)) 
        return count == n 

print(strCopies("catcowcat", "cat", 2) == True)
print(strCopies("catcowcat", "cow", 2) == False)
print(strCopies("catcowcat", "cow", 1) == True)
print(strCopies("iiijjj", "i", 3) == True)
print(strCopies("iiijjj", "i", 4) == False)
print(strCopies("iiijjj", "ii", 2) == True)
print(strCopies("iiijjj", "ii", 3) == False)
print(strCopies("iiijjj", "x", 3) == False)
print(strCopies("iiijjj", "x", 0) == True)
print(strCopies("iiiiij", "iii", 3) == True)
print(strCopies("iiiiij", "iii", 4) == False)
print(strCopies("ijiiiiij", "iiii", 2) == True)
print(strCopies("ijiiiiij", "iiii", 3) == False)
print(strCopies("dogcatdogcat", "dog", 2) == True)