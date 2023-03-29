'''
❓ PROMPT
Given an array of integers representing puzzle *pieces* and an integer *targetSize*, 
return the number of arrangements whose size sums to *targetSize*.

An arrangement is a contiguous, non-empty sequence of *pieces* within an array.

Example(s)
Input: pieces = [1,2,3], targetSize = 3
Output: 2 =, because [1, 2] and [3] are valid arrangements

Input: pieces = [1,1,1], targetSize = 2
Output: 2, because [1, 1] and [1, 1] are valid (albeit duplicate) arrangements

Input: pieces = [5, 3, 1, 4], targetSize = 8
Output: 2, because [5, 3] and [3, 1, 4] are valid arrangements
 

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
function puzzleArrangements(pieces, targetSize) {
def puzzleArrangements(pieces: list[int], targetSize: int) -> int:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''


def puzzleArrangements(pieces: list[int], targetSize: int) -> int:
    numArrangements = 0
    currentSize = 0
    sums = {}
    sums[0] = 1

    for pieceSize in pieces:
        currentSize += pieceSize

        if currentSize - targetSize in sums:
            numArrangements += sums[currentSize - targetSize]

        if currentSize in sums:
            sums[currentSize] += 1
        else:
            sums[currentSize] = 1

    return numArrangements


print(puzzleArrangements([5, 1, 3, 3, 6, 1, 5, 2, 4], 6))
