'''
❓ PROMPT
Given three words, determine if the third word is potentially a portmanteau of the first two.

A portmanteau (https://en.wikipedia.org/wiki/Portmanteau) is a word that is made by taking the start of one word and the end of another and mashing them together.\
    Brunch is a great example, combining the first 2 letters of "breakfast" with the last 4 of "lunch".

Compound words aren't considered portmanteaus, so "football" is not a portmanteau of "foot" and "ball". At least one of the two words needs to be truncated.

Example(s)
isPortmanteau("smoke", "fog", "smog") == True (sm + og)
isPortmanteau("snake", "fog", "smog") == False
isPortmanteau("lunch", "breakfast", "brunch") == True (br + unch)
isPortmanteau("shrink", "inflation", "shrinkflation") == True (shrink + flation)
isPortmanteau("foot", "ball", "football") == False
 
🛠️ IMPLEMENT
function isPortmanteau(word1, word2, proposed) {
def isPortmanteau(word1: str, word2: str, proposed: str) -> bool:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
# smoke + fog => smog sm + og 
# snake + fog !=> smog 
# lunch + breakfast => brunch br + unch 

def helper(word1:str,word2:str,proposed:str) -> bool:
    if len(word1)+len(word2) < len(proposed):
        return False 
    
    lw1 = 0
    lw2 = 1
    rw2 = 2 
    
    for rw1 in range(1,len(word1)+1):
        test = word1[lw1:rw1]
        while rw2 <= len(word2):
            test2 = word2[lw2:rw2]
            if test + test2 == proposed:
                return True 
            rw2 += 1 
            if rw2 == len(word2):
                while lw2 < rw2:
                    if test + word2[lw2:rw2] == proposed:
                        return True 
                    lw2 += 1
        rw2 = 2
    return False 
    
    
    
def isPortmanteau(word1: str, word2: str, proposed: str) -> bool:
    word1_combinations = helper(word1,word2,proposed)
    word2_combinations = helper(word2,word1,proposed)
    
    return word1_combinations or word2_combinations

def isPortmanteau(word1: str, word2: str, proposed: str) -> bool:
    def check(w1: str, w2: str):
        p1 = 0
        while p1 < len(w1) and proposed[p1] == w1[p1]:
            p1 += 1
        p1 -= 1 # the loop iterated 1 too far

        p2 = len(proposed) - 1
        s2 = len(w2) - 1
        while s2 >= 0 and proposed[p2] == w2[s2]:
            s2 -= 1
            p2 -= 1

        return p1 >= p2

    # Rule out compounds
    if proposed == word1 + word2: return False
    if proposed == word2 + word1: return False

    # The portmanteau can't exactly match either source word
    if proposed == word1 or proposed == word2: return False

    return check(word1, word2) or check(word2, word1)

print(isPortmanteau("smoke", "fog", "smog"))
print(isPortmanteau("snake", "fog", "smog"))
print(isPortmanteau("lunch", "breakfast", "brunch"))
print(isPortmanteau("shrink", "inflation", "shrinkflation"))