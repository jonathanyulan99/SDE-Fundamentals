'''
Given two strings s and t, return true if they are equal when both are typed into empty text editors.
'#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

'''
from functools import reduce
import functools

def backspaceCompare(s: str, t: str) -> bool:
    # this is going to take in every value from s/t 
    # our inital [] is what we pass to reduce as what we are going to give it back 
    def back(output,element):
        if element != '#':
            output.append(element)
        elif output:
            output.pop()
        return output 
    # reduce 
    # reduce(function,sequence,initial_value)
    # If initial is present, it is placed before the items of the sequence in the calculation, \
        # and serves as a default when the sequence is empty.
    reduce()
    return functools.reduce(back,s,[]) == reduce(back,t,[])

    '''
    s_backspaced = []
    t_backspaced = []
        
    for i in range(len(s)):
        if s[i] == '#':
            if s_backspaced:
                s_backspaced.pop()
        else:
            s_backspaced.append(s[i])
            
    for i in range(len(t)):
        if t[i] == '#':
            if t_backspaced:
                t_backspaced.pop()
        else:
            t_backspaced.append(t[i])
        
        return s_backspaced == t_backspaced
    '''


