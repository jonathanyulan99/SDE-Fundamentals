
'''
❓ PROMPT
We'll say that a "skipped pair" in a string is two instances of a char separated by a char. So "AxA" the A's make a pair. 
Pair's can overlap, so "AxAxA" contains 3 skipped pairs -- 2 for A and 1 for x. Recursively compute the number of skipped pairs in the given string.

Example(s)
countSkippedPairs("axa") == 1
countSkippedPairs("axax") == 2
countSkippedPairs("aaa") == 1
 

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
function countSkippedPairs(word) {
def countSkippedPairs(word: str) -> int:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
def countSkippedPairs(word: str) -> int:
    skipped_pairs = 0 
    if word:
        def countSkippedPairs2(word,i):
            nonlocal skipped_pairs 
            if len(word[i:]) <= 2:
                return
        
            if word[i] == word[i+2]:
                skipped_pairs+=1
        
            countSkippedPairs2(word,i+1)
        
        countSkippedPairs2(word,0)
    return skipped_pairs

print(countSkippedPairs("axa") == 1)
print(countSkippedPairs("axax") == 2)
print(countSkippedPairs("aaa") == 1)
print(countSkippedPairs("axa") == 1)
print(countSkippedPairs("axax") == 2)
print(countSkippedPairs("axbx") == 1)
print(countSkippedPairs("hi") == 0)
print(countSkippedPairs("hihih") == 3)
print(countSkippedPairs("ihihhh") == 3)
print(countSkippedPairs("ihjxhh") == 0)
print(countSkippedPairs("") == 0)
print(countSkippedPairs("a") == 0)
print(countSkippedPairs("aa") == 0)
print(countSkippedPairs("aaa") == 1)

# without use of nonlocal variable 
def countSkippedPairs(word: str) -> int:
    if not word:
        return 0 
    def helper(word,start):
        # base case start is what is being passed and incremented 
        if len(word) <= start + 2:
            return 0 
        if word[start] == word[start+2]:
            return 1 + helper(word,start+1)
        return helper(word,start+1)
    return helper(word,0)
    
print(countSkippedPairs("axa") == 1)
print(countSkippedPairs("axax") == 2)
print(countSkippedPairs("aaa") == 1)
print(countSkippedPairs("axa") == 1)
print(countSkippedPairs("axax") == 2)
print(countSkippedPairs("axbx") == 1)
print(countSkippedPairs("hi") == 0)
print(countSkippedPairs("hihih") == 3)
print(countSkippedPairs("ihihhh") == 3)
print(countSkippedPairs("ihjxhh") == 0)
print(countSkippedPairs("") == 0)
print(countSkippedPairs("a") == 0)
print(countSkippedPairs("aa") == 0)
print(countSkippedPairs("aaa") == 1)