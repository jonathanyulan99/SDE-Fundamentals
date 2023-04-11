'''
❓ PROMPT
Given a two dimensional array, output a new one dimensional array with the elements of the input in zig zag order. 
This means that the first row will be in the output from first to last, but the second row will be the reverse, 
last to first, then the third is back to normal order again, each row the opposite order of the ones before and after.

Example(s)
const matrix = [
  [1, 2, 3],
  [4, 5, 6]
]
linearizeZigZag(matrix) == [1,2,3,6,5,4]
 

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
function linearizeZigZag(matrix) {
def linearizeZigZag(matrix: list[list[int]]) -> list[int]:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.


const matrix = [
  [1, 2, 3],
  [4, 5, 6]
]
linearizeZigZag(matrix) == [1,2,3,6,5,4]
'''
matrix = [
  [1, 2, 3],
  [4, 5, 6]
]
# [0][0],[0][1],[0][2]
# [1][2],[1][1],[1][0]
# [2][0],[2][1],[2][2]
# [3][2],[3][1],[3][0]

def linearizeZigZag(matrix: list[list[int]]) -> list[int]:
    zig_zag = False 
    result = []
    for row in range(len(matrix)):
        end_value = len(matrix[0])-1
        for col in range(len(matrix[row])):
            if zig_zag:
            # instead of utilzing boolean can use modulus 
            # odd number of rows 
            # row % 2 == 1: 
            # row % 2 != 0: 
                #result.append(matrix[row][len(matrix[row])-1-col])
                result.append(matrix[row][end_value])
                end_value -= 1 
            else:
                result.append(matrix[row][col])
        zig_zag = not zig_zag
    
    return result 

print(linearizeZigZag(matrix))
matrix = [[]]
print(linearizeZigZag(matrix) == [])

matrix = [[1]]
print(linearizeZigZag(matrix) == [1])

matrix = [[1, 2, 3]]
print(linearizeZigZag(matrix) == [1,2,3])

matrix = [
  [1],
  [4],
  [7]]
print(linearizeZigZag(matrix) == [1,4,7])

matrix = [
  [1, 2, 3],
  [4, 5, 6]]
print(linearizeZigZag(matrix) == [1,2,3,6,5,4])

matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]]
print(linearizeZigZag(matrix) == [1,2,3,6,5,4,7,8,9])