matrix = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15]
]

def row_major_traversal(matrix:list[list[int]])->tuple:
    _total_row_sum = 0 
    for row in range(len(matrix)):
        _sum = 0 
        for col in range(len(matrix[row])):
            print(matrix[row][col],end=' ')
            _sum += matrix[row][col]
        _total_sum += _sum
        print(_sum)
    return (_total_row_sum,_sum)

# [5,4,3,2,1] --> [0][4] , [0][3] , [0][2] , [0][1], [0][0]
# [10,9,8,7,6]
def row_major_traversal_starting_at_back(matrix:list[list[int]])->tuple:
    _total_row_sum = 0 
    for row in range(0,len(matrix)):
        _row_sum = 0
        for col in range(len(matrix[0])-1,-1,-1):
            print(matrix[row][col],end=' ')
            _row_sum += matrix[row][col] 
        print(_row_sum)
        _total_row_sum += _row_sum 
    return (_total_row_sum,_row_sum)

# [11,12,13,14,15]
def row_major_traversal_reverse_beg(matrix:list[list[int]])->tuple:
    row = len(matrix)-1 
    _total_row_sum = 0 
    while row >= 0:
        _row_sum = 0 
        col = 0 
        while col <= len(matrix[0])-1:
            print(matrix[row][col], end= ' ')
            _row_sum += matrix[row][col]
            col+=1 
        _total_row_sum += _row_sum 
        print(_row_sum)
        row-=1 
    return (_total_row_sum,_row_sum)

# [15,14,13,12,11] -> [2][4] ,[2][3],[2][2],[2][1],[2][0]
def row_major_traversal_reverse_end(matrix:list[list[int]])->tuple: 
    row = len(matrix) - 1 
    _row_total_sum = 0
    while row >= 0: 
        _row_sum = 0 
        col = len(matrix[0]) - 1 
        while col >= 0:
            print(matrix[row][col],end=' ')
            _row_sum += matrix[row][col]
            col -= 1 
        print(_row_sum)
        _row_total_sum += _row_sum 
        row -= 1 
    return (_row_total_sum,_row_sum)

# 00 10 20
# 01 11 21 

def col_major_traversal(matrix:list[list[int]])->tuple:
    _total_col_sum = 0
    for row in range(len(matrix[0])):
        _col_sum = 0 
        for col in range(len(matrix)):
            print(matrix[col][row],end=' ')
            _col_sum += matrix[col][row]
        print(_col_sum)
        _total_col_sum += _col_sum 
    return (_total_col_sum,_col_sum)


def col_major_traversal_reverse(matrix:list[list[int]])->tuple:
    _total_col_sum = 0
    row = 0 
    while row < len(matrix[0]):
        _col_sum =0 
        col = len(matrix)-1 
        while col >= 0:
            print(matrix[col][row], end= ' ')
            _col_sum += matrix[col][row] 
            col -= 1 
        _total_col_sum += _col_sum 
        print(_col_sum)
        row +=1 
    return (_total_col_sum,_col_sum)  
    
    
# [1,2,3,4,5]
# [6,7,8,9,10]
# [11,12,13,14,15] 

# [5,10,15] -> [0][4] , [1][4], [2][4]
# [4,9,14] -> [0][3] , [1][3] , [2][3]

def col_major_traversal_reverse_beg(matrix:list[list[int]])->tuple:
    row = len(matrix[0])-1
    _total_col_sum =0 
    while row >= 0:
        col = 0
        _col_sum =0 
        while col < len(matrix):
            print(matrix[col][row],end=' ')
            _col_sum += matrix[col][row] 
            col+=1 
        _total_col_sum += _col_sum
        print(_col_sum)
        row-=1 
    print(_total_col_sum,_col_sum)
    return (_total_col_sum,_col_sum)

# [1,2,3,4,5]
# [6,7,8,9,10]
# [11,12,13,14,15] 

# [15,10,5] -> [2][4] , [1][4] , [0][4]
def col_major_traversal_starting_at_end(matrix:list[list[int]])->tuple:
    _total_col_sum =0 
    for row in range(len(matrix[0])-1,-1,-1):
        _col_sum = 0 
        for col in range(len(matrix)-1,-1,-1):
            print(matrix[col][row],end= ' ')
            _col_sum += matrix[col][row] 
        print(_col_sum)
        _total_col_sum += _col_sum 
    return (_total_col_sum,_col_sum)


