'''
PROMPT
Let's practice some basic skills in manipulating arrays and dealing with indices.
 We're going to iterate through the array and print out the values. 
 Then we'll work through some variations that will help you get comfortable working with indices.

Use an input array of [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] to verify the output easily. For the variations with a k parameter, use values of 1 through 10.

1. Print out every value
2. Print out every other value
3. Print out every other value, skipping the first one
4. Add a second parameter, k, and now print out every kth value, starting with the first.

Finally, print all of these again in *reverse*:
1. Every element starting with the last
2. Every other element starting with the last index
3. Every other element skipping the last index
4. Every kth element starting with the last

#### 🥅 Goal
Write this code as cleanly as possible with no special cases or if-statements, just choosing the starting index, increment expression, and ending condition for each loop.

**Important note for Python programmers**: 
Do not use a for loop with the range() function for this task. Python's for loop is actually what other languages call a for-each loop. 
The way that the range() function combines with this loop is very convenient but understanding and practicing these basic counting loop patterns is very important.

Instead, do this manually by manipulating an index variable directly and use a while loop.  
Building this level of understanding now will make a lot of things easier later, and will even help you better understand and write more
idiomatic Python using range().

Example(s)
testData = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k=3

printEveryKth(testData, k)

0,3,6,9
 

🔎 EXPLORE
List your assumptions & discoveries:
 

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
def printArray(array: list[int]) -> None:
def printEveryOtherValue(array: list[int]) -> None:
def printEveryOtherValueSkipFirst(array: list[int]) -> None:
def printEveryKth(array: list[int], k: int) -> None:
def printReverse(array: list[int]) -> None:
def printReverseEveryOtherValue(array: list[int]) -> None:
def printReverseEveryOtherValueSkipLast(array: list[int]) -> None:
def printReverseEveryKth(array: list[int], k: int) -> None:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

# Explore
# List your assumptions & discoveries:
# 1. Array of Integer Values
# 2. No Negative Values
# 3. Numbers are not in any sorted order, they just happen to be in order and sequential in nature
# 4. Index 0 Based
# 5. Continous offset and in memory
# 6. We have to print in order

# Insightful & revealing test cases:
# 1. []
# 2. [single_input_value]
# 3. k = 0
# 4. k is a negative number

# Brainstorm
# What approaches could work?
# Algorithm 1:
# While loop starting at zero(0) and then stopping once it gets out of range at index 10, last index printed is 9
# While loop starting at len(testData) => index_of_last_element + 1, we loop and print until we get to last value by stopping when itr is not greater than zero. Need another user_variable that increments and starts at zero
# While loop starting at len(testData) - 1 => index_of_last_element, we loop and print until we get to zero and print out the zero. Need another user_variable that incremenets and starts at zero
# print out the testData[itr_value]
# Time: O(N)
# Space: O(1)

# Plan
# Outline of algorithm #:
# One variable max_index assigned to len(testData)-1 = 9 and another variable start assigned to zero
# while loop at zero <= last_index(9) or while loop at zero < len(testData(10))
# print out the testData[start]
# increment start after printing

# Implement

# Verify
testData = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 3


def printArray(array: list[int]) -> None:
    start = 0
    end = len(testData)

    while start < end:
        print(testData[start], end=' ')
        start += 1
    print()


printArray(testData)  # verified with testData

# ----------------------------------------------

# Explore
# List your assumptions & discoveries:
# 1. Print every other value in the array in sequential order
# 2. start at the first value
# 3. skip the value in between the first and third value if a third and first value exist
# 4. There is always a value in the list
# 5. There is an odd number of values in the list, should return an odd number of values back
# 6. Half the length of the list should be printed

# Insightful & revealing test cases:
# 1. []
# 2. [1,2,3] -> odd number of values
# 3. [1,2] -> even number of values
# 4. [1] -> only one value

# Brainstorm
# start at 0
# while loop until the end of the list, or the len(list) but doesn't include that value because index zero based
# increment the start by 2 because we need to skip the middle value
# Time: O(N)/2 still O(N) cause we have to go through the whole list
# Space: O(1) shouldn't need more space

# Plan
# start variable set to zero
# while loop going till the start < len(array)
# print(array[start])
# increment start by an offset of 2


def printEveryOtherValue(array: list[int]) -> None:
    start = 0
    end = len(array)

    while start < end:
        print(array[start], end=' ')
        start += 2
    print()


# Verified
printEveryOtherValue(testData)

# Explore
# 1. Print every other value in the array in sequential order
# 2. start at the second value, we will skip the first value
# 3. skip the first value, print the second value in the list as the start
# 4. There is always a value in the list, if there is only one then return []
# 5. There is an odd number of values in the list, should only return even number of values back
# 5.5 If 5 numbers => [0,1,2,3,4] first value is skipped then [1,3] thus even
# 6. The odd number will return the same number of values as the same_odd_number + 1

# [] -> []
# [1] -> []
# [1,2] -> [2]
# [1,2,3] -> [2]
# [1,2,3,4] -> [2,4]
# [1,2,3,4,5] -> [2,4]


# BrainStorm
# start_value_index is 1 here instead of zero
# A while loop that continues to go while the start_value_index < len(testData)
# print testData[start_value_index]
# because we need to print out every other value then increment by 2 instead of 1

# Plan
# start = 1
# while start < len(testData)
# print(array[start])
# increment start by 2

# Implement

def printEveryOtherValueSkipFirst(array: list[int]) -> None:
    start = 1
    end = len(array)

    while start < end:
        print(array[start], end=' ')
        start += 2
    print()


# Verify
printEveryOtherValueSkipFirst(testData)

# Explore
# List your assumptions & discoveries:
# 1. Array of integers that are in order
# 2. Array of integers that are in sequential order
# 3. K will be a value that is one or above
# 4. K will not be a zero value
# 5. The max number K can be is the last_index of the list or len(list) - 1
# 6. The list will always print out 1 value because it starts at the first value
# 7. If K is 1 then it will just normally print out the list

# Insightful & revealing test cases:
# [],k=1 -> []
# [0],k=1 -> [0]
# [0],k=3 -> [0]
# [0,1,2] ,k=2 -> [0,2]
# [0,1,2] ,k=1 -> [0,1,2]
# [0,1,2] ,k=11 -> [0]

# Brainstorm
# Have a start variable at zero, we always print out zero
# Have the ending value be the len(list)
# while loop goes to the len(list) - 1 or < len(list)
# print inside the loop
# increment then by the k value here

# Plan
# start variable is zero
# end variable is len(array)
# while loop start < end:
# print(array[start])
# increment start variable by k

# Implement


def printEveryKth(array: list[int], k: int) -> None:
    start = 0
    end = len(array)

    while start < end:
        print(array[start], end=' ')
        start += k
    print()


# Verify
printEveryKth(testData, k)

# Explore
# List your assumptions & discoveries:
# 1. We start at the end of the list printing
# 2. Our first element we print is always the last one
# 3. If there is only one element in the list then it is inherently the last one
#
# Insightful & revealing test cases:
# 1. [] -> []
# 2. [0,1] -> [1,0]
# 3. [0] -> [0]

# Brainstorm
# start variable has to be the last_index or the len(list) - 1
# end variable is now zero but we need to include zero
# while loop that executes start is greater than or equal to end
# print(array[start])
# decrement start value by one

# Implement
# declare a start variable at len(list) - 1
# declare an end variable at zero
# while loop start >= end
# print(array[start])
# decrement start -= 1


def printReverse(array: list[int]) -> None:
    start = len(array) - 1
    end = 0

    while start >= end:
        print(array[start], end=' ')
        start -= 1
    print()


# Verify
printReverse(testData)


def printReverseEveryOtherValue(array: list[int]) -> None:
    start = len(array) - 1
    end = 0

    while start >= end:
        print(array[start], end=' ')
        start -= 2
    print()


printReverseEveryOtherValue(testData)


def printReverseEveryOtherValueSkipLast(array: list[int]) -> None:
    start = len(array) - 2
    end = 1

    while start >= end:
        print(array[start], end=' ')
        start -= 2
    print()


printReverseEveryOtherValueSkipLast(testData)
printReverseEveryOtherValueSkipLast([10])
printReverseEveryOtherValueSkipLast([0, 10])


def printReverseEveryKth(array: list[int], k: int) -> None:
    start = len(array) - 1
    end = 0

    while start >= end:
        print(array[start], end=' ')
        start -= k
    print()


printReverseEveryKth(testData, k)
printReverseEveryKth(testData, 10)
printReverseEveryKth(testData, 1)
printReverseEveryKth(testData, 20)
