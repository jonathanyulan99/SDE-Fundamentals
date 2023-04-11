
'''
❓ PROMPT
Given a square matrix *mat*, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal 
*that are not part of the primary diagonal*.

Example(s)
Input:
[[1,2,3],
 [4,5,6],
 [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Element mat[1][1] = 5 is counted only once.

Input:
[[1,1,1,1],
 [1,1,1,1],
 [1,1,1,1],
 [1,1,1,1]]
Output: 8

Input: [[5]]
Output: 5
 
🛠️ IMPLEMENT
function diagonalSum(matrix) {
def diagonalSum(matrix: list[list[int]]) -> int:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.
[
    [1,2,3]
    [4,5,6]
    [7,8,9]
]
answer = [0][0] + [len(matrix)][len(matrix[0])] + [1][1] + [1][1] + [len(matrix)-1][len(matrix)-1]
'''
matrix = [
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1]
]
def diagonalSum(matrix: list[list[int]]) -> int:
    if len(matrix) == 0:
        return 0
    num_of_rows = len(matrix)-1
    num_of_cols = len(matrix[0])-1
    
    if len(matrix[0])==1: 
        return matrix[num_of_rows][num_of_cols]
    
    result = 0
    for index in range(len(matrix[0])):
        if index == (num_of_cols-index):
            result+= matrix[index][index] 
        else:
            result += matrix[index][index] + matrix[num_of_cols-index][num_of_cols-index] 
    
    return result 

mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]
print(diagonalSum(mat) == 25)

mat = [[1,1,1,1],
       [1,1,1,1],
       [1,1,1,1],
       [1,1,1,1]]
print(diagonalSum(mat) == 8)

mat = [[5]]
print(diagonalSum(mat) == 5)

mat = []
print(diagonalSum(mat) == 0)