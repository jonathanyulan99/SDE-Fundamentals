'''
❓ PROMPT
Define a subsequence of a string "s" to be a list of characters from "s" such that the characters appear in the same order in the list and in "s".

For instance, for the string "abcd", "a", "ab", and "acd" are valid subsequences, whereas "db" is not, since "b" comes before "d" in the original string.

Given an input string, return all subsequences except the empty string.

Example(s)
getAllSubsequences("abc") ==
  ["a", "b", "c", "ab", "ac", "bc", "abc"]
 

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
function getAllSubsequences(word) {
def getAllSubsequences(word: str) -> list[str]:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.
'''
def getAllSubsequences(word: str) -> list[str]:
    result = []
    if word: 
        def helper(word,subseq,i,result): 
            if len(word) == i:
                # also can check for the subseq as well 
                # can do is subseq == '':
                    #   return 
                if len(subseq) > 0:
                    result.append(subseq) 
                return 

            helper(word,subseq,i+1,result)
            helper(word,subseq+word[i],i+1,result)
            
        helper(word,'',0,result)
    return result 

print(getAllSubsequences("abc"))

# use a set for results to make them order agnostic
print(getAllSubsequences("") == [])
print(getAllSubsequences("a") == ["a"])
print(set(getAllSubsequences("ab")) == set(["b","a","ab"]))
print(set(getAllSubsequences("abc")) == set(["c","b","bc","a","ac","ab","abc"]))
print(set(getAllSubsequences("abcd")) == set(["d","c","cd","b","bd","bc","bcd","a","ad","ac","acd","ab","abd","abc","abcd"]))
print(set(getAllSubsequences("1A")) == set(["A","1","1A"]))
print(set(getAllSubsequences("1A2b")) == set(["b","2","2b","A","Ab","A2","A2b","1","1b","12","12b","1A","1Ab","1A2","1A2b"]))
print(len(getAllSubsequences("jesitony")) == 255)
