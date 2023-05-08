def permute(nums):
    # define a helper function for backtracking
    def backtrack(start):
        # base case: add the current permutation to the result
        if start == len(nums):
            result.append(nums[:])
        # recursive case: swap each element with the first element, then recurse
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]

    result = []
    backtrack(0)
    return result

n = [1,2,3]
# subsets are different that permuations 
# subsets can be empty
# permtuations must be equal in length to the input 
'''
The main difference is that there is not the length condition, 
(remember that a subset/combination can be empty and/or have less elements than the input set
- whereas a permutation must be equal in length to the input).

Permutation - is a rearrangement of elements 
abc 
acb 
bac
bca
cab
cba
Elements ! 
N ! 
'''
print(permute(n))