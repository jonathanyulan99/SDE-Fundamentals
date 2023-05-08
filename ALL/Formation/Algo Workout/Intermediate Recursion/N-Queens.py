class Solution:
    '''
    [1,3,0,2]
    [1st Queen is on the (0-index +1)1st row and the (O-index +1) 2nd column]
    [2nd Queen is on the 2nd row and the 4th Column]
    [3rd Queen is on the 3rd row and the 1st Column]
    [4th Queen is on the 4th row and 3rd Column]
    The position of the Queens in a 1-D Array on 4 x 4 Array
    
    [2,0,3,1]
    1st Queen - 1st Row, 3rd Column 
    2nd Queen - 2nd Row, 1st Column
    3rd Queen - 3rd Row, 4th Column 
    4th Queen - 4th Row, 2nd Column 
    The position of the Queen is located on the 0+1 Row based on the index 
    The column position of the Queen is COL-1 due to the 0 index of the Array 
    '''
    def solveNQueens(self,n:int)->list[list[str]]:
        solutions = [] 
        state = [] # starting state is empty list cause no Queens have been placed
        self.search(state,solutions,n)
        return solutions 
    
    # is_valid_state for a state to be valid all N QUEENS need to be placed on the board
    # so state is [] == N then its true 
    def is_valid_state(self,state,n):
        return len(state) == n
    
    # our conditions for no queens can attack one another will be handled here
    def get_candidates(self,state,n):
        if not state: 
            return range(n) 
        
        # if state is not empty 
        # find hte next position in the state to populate
        position = len(state) 
        candidates = set(range(n)) 
        
        # prune down candidates taht place the queen into attacks
        for row,col in enumerate(state):
            # discard the col index if it's occupied 
            candidates.discard(col)
            dist = position - row 
            # discard diagnoals  
            candidates.discard(col+dist)
            candidates.discard(col-dist) 
        return candidates 
    
    def search(self,state,solutions,n):
        if self.is_valid_state(state,n):
            solutions.append(self.state_to_string(state,n))
            return 

        for candidate in self.get_candidates(state,n):
            # recursive step
            state.append(candidate)
            self.search(state,solutions,n)
            # pop our last step 
            state.pop()
        
    
    def state_to_string(self,state,n):
        # ex: [1,3,0,1]
        # output: [".Q..","...Q","Q...","..Q."]
        output = [] 
        for i in state:
            string = '.' * i + 'Q' + '.' * (n-i-1) 
            output.append(string) 
        return output 