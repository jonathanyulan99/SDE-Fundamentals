'''
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one 
with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the number of rows and the
number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same 
row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the 
new reshaped matrix; Otherwise, output the original matrix.

'''
def matrixReshape(mat: list[list[int]], r: int, c: int) -> list[list[int]]:
    temp = []
    
    # create a temporary list to hold all the values of our matrix
    for row in range(len(mat)):
        for col in range(len(mat[row])):
            temp.append(mat[row][col])
    
    if r * c != len(temp):
        return mat 
    
    outside_list = [] 
    idx = 0
    for row in range(r):
        inside_list = [] 
        for col in range(c):
            inside_list.append(temp[idx])
            idx += 1 
        outside_list.append(inside_list)
    
    return outside_list 

# mat = [[1,2],[3,4]], r = 2, c = 4
new_matrix = matrixReshape([[1,2,3,4]],1,4)
print(new_matrix)