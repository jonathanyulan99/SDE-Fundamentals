'''
In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. 
(A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

Return the minimum number of rotations so that all the values in tops are the same, or all the values 
in bottoms are the same.

If it cannot be done, return -1.
'''
def minDominoRotations(tops: list[int], bottoms: list[int]) -> int:
    tops_dict = {i:0 for i in range(1,7)}
    bots_dict = {i:0 for i in range(1,7)}
    same_dict = {i:0 for i in range(1,7)}
    
    n = len(tops)
    
    for i in range(len(tops)):
        top_value = tops[i]
        bot_value = bottoms[i]
        if top_value == bot_value:
            same_dict[top_value] += 1
        else:
            tops_dict[top_value] += 1 
            bots_dict[bot_value] += 1
    
    
    for i in range(1,7):
        if tops_dict[i] + bots_dict[i] - same_dict[i] == n:
            return n - max(tops_dict[i], bots_dict[i])
    
    return -1
    
        
    
    
    
tops = [2,1,2,4,2,2]
bottoms = [5,2,6,2,3,2]
print(minDominoRotations(tops,bottoms))
tops = [3,5,1,2,3]
bottoms = [3,6,3,3,4]
print(minDominoRotations(tops,bottoms))