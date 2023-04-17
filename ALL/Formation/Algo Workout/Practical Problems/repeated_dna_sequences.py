'''
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) 
that occur more than once in a DNA molecule. You may return the answer in any order.
'''

def find_subsequnces(s:str)->list[str]:
    past_visited = {} 
    output = [] 
    for i in range(len(s)-9):
        sequence = s[i:i+10] 
        if sequence in past_visited:
            if not past_visited[sequence]:
                # change it so we only add it once 
                past_visited[sequence] = True 
                output.append(sequence) 
        else:
            past_visited[sequence] = False
    return output
