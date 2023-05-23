class Solution:
        def __init__(self,row,col,tq,qpsf,ans):
            self.row = row
            self.col = col
            self.tq = tq
            self.board = [[0]*self.tq for _ in range(self.tq)]
            self.qpsf = qpsf
            self.ans = ans 
        
        def solve(self,board,row,col,tq,qpsf,ans):
            if qpsf == tq:
                print(ans)
                return
            
            if col == len(board[0]):
                col = 0 
                row += 1
                
            if row == len(board):
                return 
            
            
            if self.is_valid(board,row,col):
                board[row][col] = True
                self.solve(board,row,col+1,tq,qpsf+1,ans + '[' + str(row) + ',' + str(col) + ']')
                board[row][col] = False 
            
            # if it's not valid 
            # try the next column 
            self.solve(board,row,col+1,tq,qpsf,ans)
            
        
        def is_valid(self,board,row,col):
            # vertically above 
            r = row - 1
            c = col 
            
            while(r >= 0):
                if board[r][c]:
                    return False 
                r-=1 
            
            
            #horizontally left 
            r1 = row 
            c1 = col - 1 
            
            while (c1 >= 0):
                if board[r1][c1]:
                    return False 
                c1-=1 
            
            #diagnoally left 
            r = row - 1 
            c = col - 1 
            while(r >= 0 and c>=0):
                if board[r][c]:
                    return False 
                r-=1
                c-=1 
            
            #diagnolly right 
            r = row - 1 
            c = col + 1 
            while(r>=0 and c<len(board[0])):
                if board[r][c]:
                    return False 
                r -= 1 
                c += 1 
            
            return True 
    
    
    

nQueens = Solution(0,0,4,0,'')
nQueens.solve(nQueens.board,0,0,4,0,'')