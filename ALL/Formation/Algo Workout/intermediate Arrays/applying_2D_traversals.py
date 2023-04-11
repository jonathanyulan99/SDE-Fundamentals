'''
❓ PROMPT
In this task, we're going to apply basic 2-dimensional matrix traversals to solve some simple problems. 
While working on these, look out for other patterns you may have seen previously. 
Each of these takes the row- and column-major traversals and composites them with simpler ideas you have almost certainly encountered 
in one-dimensional problems.

This task is two similar problems in one:
- First, write a function that returns the average of the smallest values in each _column_.
- Write a new version of this function that returns the average of the smallest value in each _row_.

Remember that since we represent a matrix as nested arrays (an array of arrays), 
many problems on a matrix can be broken down into two array patterns. This makes them easier to reason about and code. 

Example(s)
matrix = [
  [32, 23, 3],
  [23,  7, 5]
]
averageColumnMinimum(matrix) == 11 (because average(23, 7, 3) = 11)
averageRowMinimum(matrix) == 4 (because average(5, 3) = 4)
 

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
function averageColumnMinimum(matrix) {
function averageRowMinimum(matrix) {

def averageColumnMinimum(matrix: list[list[int]]) -> float:
def averageRowMinimum(matrix: list[list[int]]) -> float:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

matrix = [
  [32, 23, 3],
  [23,  7, 5]
]
'''
matrix = [
    [32,23,3],
    [23,7,5]
]

# iterate through the matrix row 
# _row_min_values = 0  
# check for matrix[0][0] , matrix[0][1].... matrix[0][len(matrix[0])-1]
# _row_min_value = float('inf') 
# check against the values and updated minimum if our minimum is larger than the minimum there 
# _row_min_value += _row_min_value 
def averageRowMinimum(matrix: list[list[int]]) -> float:
    # base case if there is a matrix [[]]
    if len(matrix[0])==0:
        return 0 
    
    # hold all of our minimum row values and then average based on the number of rows 
    # number of rows len(matrix) is what we divide later against 
    _row_min_values = 0 
    for row in range(0,len(matrix)):
        _row_min_value = float('inf')
        for col in range(0,len(matrix[row])):
            _row_min_value = min(_row_min_value,matrix[row][col])
        _row_min_values += _row_min_value 

    return _row_min_values/len(matrix)

print(averageRowMinimum(matrix))

def averageColumnMinimum(matrix: list[list[int]]) -> float:
    if len(matrix[0])==0:
        return 0 
    
    _col_min_values = 0 
    for row in range(len(matrix[0])):
        _col_min_value = float('inf')
        for col in range(len(matrix)):
            _col_min_value = min(_col_min_value,matrix[col][row])
        _col_min_values += _col_min_value 
    
    return _col_min_values/len(matrix[0])

print(averageColumnMinimum(matrix))

matrix = [[]]
print(averageColumnMinimum(matrix) == 0)
print(averageRowMinimum(matrix) == 0)

matrix = [[5]]
print(averageColumnMinimum(matrix) == 5)
print(averageRowMinimum(matrix) == 5)

matrix = [[1, 2, 3]]
print(averageColumnMinimum(matrix) == 2)
print(averageRowMinimum(matrix) == 1)

matrix = [
  [1],
  [4],
  [7]]
print(averageColumnMinimum(matrix) == 1)
print(averageRowMinimum(matrix) == 4)

matrix = [
  [5, 5, 5],
  [5, 5, 5]]
print(averageColumnMinimum(matrix) == 5)
print(averageRowMinimum(matrix) == 5)

matrix = [
  [32, 23, 3],
  [23,  7, 5]]
print(averageColumnMinimum(matrix) == 11) # average(23, 7, 3) = 11
print(averageRowMinimum(matrix) == 4) # average(5, 3) = 4

matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]]
print(averageColumnMinimum(matrix) == 2)
print(averageRowMinimum(matrix) == 4)

matrix = [
  [ 1,  2,  3,  4,  5],
  [ 6,  7,  8,  9, 10],
  [11, 12, 13, 14, 15]]
print(averageColumnMinimum(matrix) == 3)
print(averageRowMinimum(matrix) == 6)
    