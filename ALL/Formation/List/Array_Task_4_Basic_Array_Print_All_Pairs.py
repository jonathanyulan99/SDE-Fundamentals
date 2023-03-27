'''
PROMPT
Finding all pairs is one of the basic patterns that frequently comes up, especially in _brute force_ algorithms. 
Understanding and proficiently applying this pattern will often jump-start progress on other problems, even if in the end there may be a way to do something more efficiently.

To illustrate this pattern, write a function that takes an array and prints out all of the pairs of elements from the array.

Example(s)
printAllPairs([1,2,3])
(1, 2)
(1, 3)
(2, 3)

printAllPairs([1,2,3,4])
(1, 2)
(1, 3)
(1, 4)
(2, 3)
(2, 4)
(3, 4)
 

🔎 EXPLORE
List your assumptions & discoveries:
- The Input is never empty 
- The Input can contain zero, one, odd or even number of inputs 
- Note that we don't see (1,1) which means that the pairs do not include the same number 
- (first_index,first_index+1) is the start of the for loops or while loops 
- input always contains at least two values or more
- what to return in the case of the input having zero or only one value
- must return at least a pair 

Insightful & revealing test cases:
 - input is empty 
 - input only has one value 
 - an array with duplicate values such as [1,1,1] -> (1,1) & (1,1) So it always return N - N_left of values as long as N >= 2 or N > 1 
 - [1,1,1,1,1] -> (1,1) & (1,1) & (1,1) & (1,1) & (1,1) & (1,1) & (1,1) & (1,1) & (1,1) & (1,1) 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1: Using two for loops or two while loops with two different pointers.
One starting at the first_index and then the second pointer or second for loop starting at the first_index + 1
Time: O(N^2)
Space: O(1)
 

📆 PLAN
Outline of algorithm #: 
- declare a variable called index_start at zero 
- declare a second variable called index_rest which is one greater than index_start 
- while loop to begin at the index_start to the len(array)
- nested while loop to terminate when the index_rest is less than the len(array) 
- print(index_start,index_rest) 
- increment index_rest by one in the nested while loop
- increment index_start by one in outter while loop 
 

🛠️ IMPLEMENT
function printAllPairs(array) {
def printAllPairs(array: list[int]) -> None:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''


def printAllPairs(array: list[int]) -> None:
    index_start = 0
    index_rest = index_start + 1

    while index_start < len(array):
        while index_rest < len(array):
            print(array[index_start], array[index_rest])
            index_rest += 1
        index_start += 1
        # need to reset the secondary index again
        index_rest = index_start + 1
    print()


# verify
printAllPairs([])
# no output

printAllPairs([1])
# no output

printAllPairs([1, 2, 3, 4, 5])
# (1, 2)
# (1, 3)
# (1, 4)
# (1, 5)
# (2, 3)
# (2, 4)
# (2, 5)
# (3, 4)
# (3, 5)
# (4, 5)

printAllPairs([5, 8, 5, 8])
# (5, 8)
# (5, 5)
# (5, 8)
# (8, 5)
# (8, 8)
# (5, 8)
