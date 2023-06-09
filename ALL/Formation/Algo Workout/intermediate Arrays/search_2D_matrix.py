def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    num_of_cols = len(matrix[0])
    num_of_rows = len(matrix)
    
    if num_of_rows == 0:
        return False 
    
    left = 0 
    right = num_of_cols * num_of_rows -1 
    
    while left <= right:
        pivot = (left+right) // 2 
        pivot_row_index = pivot // num_of_cols
        pivot_col_index = pivot % num_of_cols 
        
        if matrix[pivot_row_index][pivot_col_index] == target:
            return True 
        else:
            if target < matrix[pivot_row_index][pivot_col_index]:
                right = pivot + 1
            else:
                left = pivot + 1 
    
    
    return False 

matrix = [[-9,-9,-9,-8,-8,-7,-6,-4,-4,-3],[0,1,2,2,4,5,5,5,7,9],[12,12,14,14,15,17,19,19,19,21],[22,23,23,25,25,26,26,28,28,29],[31,31,31,33,34,36,37,38,38,39],[40,42,43,44,46,46,46,47,49,50],[52,54,55,57,59,60,60,62,64,66],[68,68,70,71,71,72,74,76,78,80],[82,83,85,85,85,87,88,88,89,89],[90,90,90,91,93,94,94,95,95,97],[98,98,99,99,101,103,105,106,108,109],[112,112,112,113,113,113,114,116,118,118],[119,121,122,124,125,125,125,126,127,128],[131,133,134,134,134,135,135,137,137,139],[141,143,145,147,148,150,150,150,150,152],[153,153,154,155,157,157,157,159,161,162],[164,166,167,167,167,169,170,170,171,173],[176,176,178,179,181,182,183,183,184,186]]
print(searchMatrix(matrix,135))