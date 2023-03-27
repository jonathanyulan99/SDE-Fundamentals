'''
PROMPT
We'll say that a "skipped pair" in a string is two instances of a char separated by a char. 
So "AxA" the A's make a pair. Pair's can overlap, so "AxAxA" contains 3 skipped pairs -- 2 for A and 1 for x.
Recursively compute the number of skipped pairs in the given string.

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
    if len(word) <= 2:
        return 0

    count = countSkippedPairs(word[1:])
    if word[0] == word[2]:
        count += 1
    return count


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


def count_skipped_pairs(word: str) -> int:
    def helper_count_skipped_pairs(word: str, start: int):
        if len(word) <= 2+start:
            return 0
        if word[start] == word[start+2]:
            return 1 + helper_count_skipped_pairs(word, start+1)

        return helper_count_skipped_pairs(word, start+1)
    return helper_count_skipped_pairs(word, 0)


print(count_skipped_pairs("axa") == 1)
print(count_skipped_pairs("axax") == 2)
print(count_skipped_pairs("axbx") == 1)
print(count_skipped_pairs("hi") == 0)
print(count_skipped_pairs("hihih") == 3)
print(count_skipped_pairs("ihihhh") == 3)
print(count_skipped_pairs("ihjxhh") == 0)
print(count_skipped_pairs("") == 0)
print(count_skipped_pairs("a") == 0)
print(count_skipped_pairs("aa") == 0)
print(count_skipped_pairs("aaa") == 1)
