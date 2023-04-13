class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        Given M rows N columns 
        M != N or rows != columns 
        Done In Place 
        We have to find a way to iterate through the entire matrix first then change things
        We see zero then we impelement some helper function to get all the rows,cols we need to change 
        0 --> change elements in row/column to --> 1 but not change them to zero till the end 
        if we see a number != 0 ignore it 
        but if we see a zero we get the rows and columns of that space and put (1,0) 
        tuple (original_number,new_number)
        then if we iterate through our matrix again, we change it to new number 
        """
        # iterate through our m x n matrix 
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    for tmp in range(len(matrix)):
                        if matrix[tmp][col] != 0:
                            matrix[tmp][col] = "*"
                    for tmp in range(len(matrix[row])):
                        if matrix[row][tmp] != 0:
                            matrix[row][tmp] = '*'
        
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == '*':
                    matrix[row][col] = 0 

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]     
Solution = Solution()
Solution.setZeroes(matrix)
print(matrix)