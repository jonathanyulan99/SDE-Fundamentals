'''
❓ PROMPT
In mathematics when two matrices are multiplied, the result is a new matrix where each position (i, j) 
in the output is the sum of the products of the ith _row_ in the first matrix and the jth _column_ in the second.
This is called the [dot product](https://www.mathsisfun.com/algebra/matrix-multiplying.html).

As a follow-up, modify your code to support matrices that are *not* square. 
This requires that the number of columns in the first matrix be equal to the number of rows in the second 
so that the row x column cross products are possible.

Example(s)
a = [
  [1, 2],
  [3, 4]
]
b = [
  [5, 6],
  [7, 8]
]
matrixMultiply(a,b) ==
[
  [19,22],
  [43,50]
]
The (0, 0) position in the result is: 1 * 5 + 2 * 7 = 19
The (0, 1) position in the result is: 1 * 6 + 2 * 8 = 22
The (1, 0) position in the result is: 3 * 5 + 4 * 7 = 43
The (1, 1) position in the result is: 3 * 6 + 4 * 8 = 50
 

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
function matrixMultiply(a, b) {
def matrixMultiply(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

As a follow-up, modify your code to support matrices that are *not* square. 
This requires that the number of columns in the first matrix be equal to the number of rows in the second 
so that the row x column cross products are possible.

a = [
  [1, 2],
  [3, 4]
]
b = [
  [5, 6],
  [7, 8]
]
matrixMultiply(a,b) ==
[
  [19,22],
  [43,50]
]
The (0, 0) position in the result is: 1 * 5 + 2 * 7 = 19
The (0, 1) position in the result is: 1 * 6 + 2 * 8 = 22
The (1, 0) position in the result is: 3 * 5 + 4 * 7 = 43
The (1, 1) position in the result is: 3 * 6 + 4 * 8 = 50

[0][0] = a[0][0] * b[0][0] + a[0][1] * b[1][0]
[0][1] = a[0][0] * b[0][1] + a[0][1] * b[1][1]
[1][0] = a[1][0] * b[0][0] + a[1][1] * b[1][0]
[1][1] = a[1][0] * b[0][1] + a[1][1] * b[1][1]
'''
a = [
    [1,2],
    [3,4]
]

b = [
    [5,6],
    [7,8]
]

def matrixMultiply(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    # check for number of columns in the first matrix ==> len(matrix[0]) 
    # == the number of rows in the second matrix ===> len(matrix)
    
    if len(a[0])!=len(b):
        return [[]] 
    
    results = []
    for x in range(len(a)):
        result = [] 
        for y in range(0,len(b[0])):
            result.append(0)
        results.append(result)

    for row in range(len(a)):
        for col in range(len(b[0])):
            # if row == 0 and col==0: 
            #     results[row][col] += ((a[row][col] * b[row][col]) + (a[row][col+1] * b[row+1][col]))
            # elif row == col-1 and col == row+1:
            #     results[row][col] += ((a[row][row] * b[row][col]) + (a[row][col] *  b[col][col]))
            # # 1 0
            # elif col==row-1 and row == col+1:
            #     results[row][col] += ((a[row][col] * b[col][col]) + (a[row][row] * b[row][col]))
            # else:
            #     results[row][col] += ((a[row][col-1] * b[row-1][col]) + (a[row][col] * b[row][col]))
            value = 0
            for k in range(len(a[0])):
                value += a[row][k] * b[k][col]
            results[row][col] = value 
    return results 

print(matrixMultiply(a,b))
a = [[]]
b = [[]]
print(matrixMultiply(a,b) == [[]] or matrixMultiply(a,b) == [[None]])

# a = [[5]]
# b = [[10]]
# print(matrixMultiply(a,b) == [[50]])

a = [
  [1, 2],
  [3, 4]]
b = [
  [5, 6],
  [7, 8]]
print(matrixMultiply(a,b) == [
  [19,22],
  [43,50]])

a = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]]
b = [
  [10, 20, 30],
  [40, 50, 60],
  [70, 80, 90]]
print(matrixMultiply(a,b) == [
  [300,360,420],
  [660,810,960],
  [1020,1260,1500]])

a = [[1, 2, 3]]
b = [
  [4],
  [5],
  [6]]
print(matrixMultiply(a,b) == [[32]])

a = [
  [1, 2, 3],
  [4, 5, 6]]
b = [
  [10, 20],
  [30, 40],
  [50, 60]]
print(matrixMultiply(a,b) == [
  [220,280],
  [490,640]])