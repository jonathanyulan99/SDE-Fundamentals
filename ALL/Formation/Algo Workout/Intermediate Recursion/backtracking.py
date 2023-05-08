# STATE is the crux of backtracking problems
# backtracking is asking you to find VALID STATES 
 
# takes in a state and decides whether the state can be a valid solution
def is_valid_state(state):
    # check if it is a valid solution
    return True 

# this functions a list of candidates to construct the next possible state
def get_candidates(state):
    return []

# RECURSIVE function 
# it calls the previous two helper functions to decide whether the state is valid 
# if it is it gives a deep copy, because we need a static snapshot of the state 
# if there is only one global solution that this search function might just return one solution 
# or may return may problems 
def search(state,solutions):
    if is_valid_state(state):
        solutions.append(state.copy())
    # if you only need one you can return right here
    # or if you need all the valid states then you need to explore all valid states 
    # return 

    for candidate in get_candidates(state):
        state.add(candidate)
        # recursive portion
        search(state,solutions)
        # here is where we would return too if that state turns out unvalid 
        # if we can not make any progress then we want to remove that that state from our list of states, because that candidate is never going to be part of the possible solution
        state.remove(candidate)

# entry point to the problem 
def solve():
    solutions = [] 
    state = set() 
    search(state,solutions)
    # returns the valid solutions 
    return solutions 
