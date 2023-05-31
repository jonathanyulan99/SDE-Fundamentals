class Solution:
    '''
    return all the paths
    '''
    def solve(row:int,col:int):
        if row == 1 or col == 1:
            return 1 
        
        left = Solution.solve(row-1,col)
        right = Solution.solve(row,col-1)
        return left + right 

solution = Solution
print(solution.solve(row=3,col=3))


 
class Solution:
    '''
    return all the paths
    '''
    lst = []
    def solve(row:int,col:int,proc=''):
        if row == 1 and col == 1:
            Solution.lst.append(proc) 
            return
        
        if row == 1:  
            for i in range(col-row):
                proc += 'R'
            Solution.lst.append(proc) 
            return 

        if col == 1:
            for i in range(row-col):
                proc+= 'D'
            Solution.lst.append(proc)
            return 
        
        Solution.solve(row-1,col,proc+'D')
        Solution.solve(row,col-1,proc+'R')
        return Solution.lst 
    
solution = Solution
print(solution.solve(row=3,col=3))

class Solution:
    '''
    return all the paths
    '''
    
    def solve_diagnol(row:int,col:int,proc=''):
        if row == 1 and col == 1:
            local_list = []
            local_list.append(proc) 
            return local_list 
        
        returned_list = [] 
        if row > 1 and col > 1: 
            returned_list.extend(Solution.solve_diagnol(row-1,col-1,proc+'D'))
        if row >1:
            returned_list.extend(Solution.solve_diagnol(row-1,col,proc+'VD'))
        if col>1:
            returned_list.extend(Solution.solve_diagnol(row,col-1,proc+'HR'))
        return returned_list  
    
solution = Solution
print(solution.solve_diagnol(row=3,col=3))

class Solution:
    '''
    return all the paths
    '''

    @staticmethod
    def solve_w_obstacles(maze: list[list[bool]], row: int, col: int, proc: str = ''):
        if row == len(maze) - 1 and col == len(maze[0]) - 1:
            local_list = []
            local_list.append(proc)
            return local_list

        if maze[row][col]:
            returned_list = []
            if row < len(maze) - 1 and col < len(maze[0]) - 1:
                returned_list.extend(Solution.solve_w_obstacles(maze, row + 1, col + 1, proc + 'D'))
            if row < len(maze) - 1:
                returned_list.extend(Solution.solve_w_obstacles(maze, row + 1, col, proc + 'VD'))
            if col < len(maze[0]) - 1:
                returned_list.extend(Solution.solve_w_obstacles(maze, row, col + 1, proc + 'HR'))
            return returned_list
        return []


solution = Solution()
board = [[True, True, True], [True, False, True], [True, True, True]]
print(solution.solve_w_obstacles(board, 0, 0))
print()

class Solution:
    '''
    return all the paths
    '''

    @staticmethod
    def solve_all_paths_w_obstacles(maze: list[list[bool]], row: int, col: int,path,step, proc: str = ''):
        if row == len(maze) - 1 and col == len(maze[0]) - 1:
            path[row][col] = step 
            local_list = []
            local_list.append(proc)
            for val in path:
                print(val)
            print(proc)
            print()
            return local_list
        
        if maze[row][col]:
            # Backtracking portion
            # make a change 
            maze[row][col] = False  
            path[row][col] = step 
            returned_list = []
            if row < len(maze) - 1 and col < len(maze[0]) - 1:
                returned_list.extend(Solution.solve_all_paths_w_obstacles(maze, row + 1, col + 1,path,step+1, proc + 'D'))
            if row < len(maze) - 1:
                returned_list.extend(Solution.solve_all_paths_w_obstacles(maze, row + 1, col,path,step+1, proc + 'B'))
            if col < len(maze[0]) - 1:
                returned_list.extend(Solution.solve_all_paths_w_obstacles(maze, row, col + 1,path,step+1, proc + 'R'))
            if row > 0: 
                returned_list.extend(Solution.solve_all_paths_w_obstacles(maze, row-1, col,path,step+1, proc + 'U'))
            if col > 0:
                returned_list.extend(Solution.solve_all_paths_w_obstacles(maze, row, col - 1,path,step+1, proc + 'L'))
            # Undoing what I did 
            # this is known as backtracking 
            # this line is where the function will be over, before the function gets removed, remove the changes that were made by that function
            # if you don't undo this portion or have it made False intially because it needs to be visited in the recursive stack without the changes made at a different recursive call stack that was popped off earlier in the function recurisve calls 
            # undo the change 
            maze[row][col] = True 
            path[row][col] = 'X'
            return returned_list
        return []

# While you are moving back, you must restore the maze as it was 
# if you do not do this then you can lead to incorrect results or lead into a recursive overstack overflow 
# when the function is returned that is when we can restore whatever data type we are using to its original state 
# Remark the cell as its Original State 
solution = Solution()
board = [[True, True, True], [True, True, True], [True, True, True]]
path = [['X' for y in range(len(board[0]))] for x in range(len(board))]
print(solution.solve_all_paths_w_obstacles(board, 0, 0,path,1))