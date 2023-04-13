'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.
'''

def matrix_rotation(matrix:list[list[int]])->None:
    r = len(matrix)
    c = len(matrix[0])
    
    # main point is diagnol switching of the values in our matrix 
    # but we  want to only switch as we move to the last row of the matrix
    # if we continue to switch on the way to the bottom we will run into a problem 
    # we will touch values that should not be touched 
    
    for row in range(r):
        # this is the key part as we want to only touch the zero row in our matrix not our zero(first) row 
        # by setting up our for loops like this we will not do any switching for any members in our matrix on our first run 
        for col in range(row):
            matrix[row][col], matrix[col][row] = matrix[col][row],matrix[row][col]
        
    # by reversing each row now we end up with the proper rotated image of 90' 
    '''
        [1,2,3]      [1,4,7]      [7,4,1]
        [4,5,6] ---> [2,5,8] ---> [8,5,2]
        [7,8,9]      [3,6,9]      [9,6,3]
    '''
    
    for row in range(r):
        mid = len(matrix[row]) // 2
        l = 0
        r = len(matrix[row])-1
        
        while l <= mid:
            matrix[row][l],matrix[row][r] = matrix[row][r],matrix[row][l]
            r -= 1
            l += 1
            
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
] 

matrix_rotation(matrix)
print(matrix)