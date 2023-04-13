'''
Reversi is a game where players place black or white discs on an 8x8 size board.

When a group of discs of one color is surrounded by dicsc of the other color on both ends, all the inner discs flip color.

***BWWWWWB***WWWW*** => ***BBBBBBB***WWWW***

A move is "legal" if making it would result in at least one disc of the opposite color to flip


Given a board with some discs placed on it, determine the numer of possible legal moves for a black turn!


  0 1 2 3 4 5 6 7
0 * * * * * * * *
1 * * * * * * * W
2 * * * * L * * *
3 * * * B W L * *
4 * * L W B * * *
5 * * * L * * * *
6 * * * * * * * *
7 * * * * * * * *

=> 4

input - grid or list of B/W coord

side to side, up and down, diagonal 

can have no B/W coord on grid (empty input)

input = [['B', 3, 3], ['W', 3, 4], ['W', 4, 3], ['B', 4, 4]]
black_input =[[3, 3]. [4,4]]
white_black = [[3,4]. [4,3]]

n = num of coordinates
m = length / width - 2

n^2 * m

counter = 0

iterate over all discs
    if the disc is black
        find white neighbours:
        iterate over all discs
          if disc is white and coordinates next to current black one
          they are neighbours
          move in the direction away form black, checking each coordinate
            if coordinate contains nothing, increase counter
            else if coordinate contains white, keep going
            else if coordinate is out of bounds, stop iteration
'''