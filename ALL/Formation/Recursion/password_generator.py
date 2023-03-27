'''
PROMPT
Given a set of characters, a minimum length, and a maximum length, generate all strings that can be 
created using characters from the set between those lengths inclusively.

This algorithm requires a large time and space complexity to enumerate all the possibilities. You should be 
able to get this to either time out or run out of memory even on rather small lengths.

Example(s)
generatePasswords(["a"], 2, 4) == [
  "aa",
  "aaa",
  "aaaa",
]

generatePasswords(["a", "b", "c"], 2, 3) == [
  "aa","aaa","aab","aac",
  "ab","aba","abb","abc",
  "ac","aca","acb","acc",
  "ba","baa","bab","bac",
  "bb","bba","bbb","bbc",
  "bc","bca","bcb","bcc",
  "ca","caa","cab","cac",
  "cb","cba","cbb","cbc",
  "cc","cca","ccb","ccc"
]
 

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
function generatePasswords(validCharacters, minLength, maxLength) {
def generatePasswords(validCharacters: list[str], minLength: int, maxLength: int) -> list[str]:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''


def generatePasswords(validCharacters: list[str], minLength: int, maxLength: int) -> list[str]:
    # storage for our final return
    # list is our output
    generated_passwords = list()

    # temporary storage to store the permutations of our validCharacter in validChracters
    # aa
    temp_password = list()

    # helper function that we are going to recurse in our main function
    def permutate():
        # base case is when our temp_password is greater than maxLength
        # we can return
        if len(temp_password) > maxLength:
            return

        # aaa -> will be like this ['a','a','a']
        # need to join the the list together and append to our output
        if len(temp_password) >= minLength and len(temp_password) <= maxLength:
            generated_passwords.append(''.join(temp_password))

        for i in range(len(validCharacters)):
            temp_password.append(validCharacters[i])
            permutate()
            temp_password.pop()
    permutate()

    return generated_passwords


print(generatePasswords(["a", "b", "c", "d"], 0, 0) == [""])
print(generatePasswords(["a", "b", "c", "d"], 0, 1)
      == ["", "a", "b", "c", "d"])
print(generatePasswords(["a", "b", "c", "d"], 1, 1) == ["a", "b", "c", "d"])
print(generatePasswords(["a", "b"], 3, 3) == [
      "aaa", "aab", "aba", "abb", "baa", "bab", "bba", "bbb"])
print(generatePasswords(["a"], 2, 4) == ["aa", "aaa", "aaaa"])
print(generatePasswords(["a"], 2, 4) == ["aa", "aaa", "aaaa"])
print(generatePasswords(["a", "b", "c"], 2, 3) == ["aa", "aaa", "aab", "aac", "ab", "aba", "abb", "abc",
                                                   "ac", "aca", "acb", "acc", "ba", "baa", "bab", "bac", "bb", "bba", "bbb", "bbc",
                                                   "bc", "bca", "bcb", "bcc", "ca", "caa", "cab", "cac", "cb", "cba", "cbb", "cbc",
                                                   "cc", "cca", "ccb", "ccc"])
print(generatePasswords(["a", "b", "c", "d"], 2, 3) == ["aa", "aaa", "aab", "aac", "aad", "ab", "aba", "abb",
                                                        "abc", "abd", "ac", "aca", "acb", "acc", "acd", "ad", "ada", "adb", "adc",
                                                        "add", "ba", "baa", "bab", "bac", "bad", "bb", "bba", "bbb", "bbc", "bbd",
                                                        "bc", "bca", "bcb", "bcc", "bcd", "bd", "bda", "bdb", "bdc", "bdd", "ca",
                                                        "caa", "cab", "cac", "cad", "cb", "cba", "cbb", "cbc", "cbd", "cc", "cca",
                                                        "ccb", "ccc", "ccd", "cd", "cda", "cdb", "cdc", "cdd", "da", "daa", "dab",
                                                        "dac", "dad", "db", "dba", "dbb", "dbc", "dbd", "dc", "dca", "dcb", "dcc",
                                                        "dcd", "dd", "dda", "ddb", "ddc", "ddd"])

print(len(generatePasswords(["a", "b", "c", "d"], 3, 4)) == 320)
print(len(generatePasswords(["a", "b", "c", "d"], 3, 5)) == 1344)
