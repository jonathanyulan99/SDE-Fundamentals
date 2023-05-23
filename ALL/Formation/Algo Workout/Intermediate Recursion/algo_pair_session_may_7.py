def permute(nums):
    # define a helper function for backtracking
    def dfs(ind):
        # base case: add the current permutation to the result
        if ind == len(nums):
            result.append(nums[:])
        # recursive case: swap each element with the first element, then recurse
        for i in range(ind, len(nums)):
            nums[ind], nums[i] = nums[i], nums[ind]
            dfs(ind + 1)
            nums[ind], nums[i] = nums[i], nums[ind]

    result = []
    dfs(0)
    return result

n = ['a','b','c']
# subsets are different that permuations 
# subsets can be empty
# permtuations must be equal in length to the input 
# permtuations are N!
# subsets are 2^N * N at best! 
# _ first postion can choose 3 values 
# _ _ second position can choose 2 values
# _ _ _ third position can choose only 1 value left 
# 3*2*1 
# N * (N-1) .... * 1 = N!  
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

class Solution:
    def permutations(self,nums:list[int])->list[list[int]]:
        result = [] 
        if len(nums) == 1:
            return [nums[:]]
        
        for _ in range(len(nums)):
            n = nums.pop(0) 
            perms = self.permutations(nums)
            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)
            
        return result 
    
solve = Solution()
n1 = [1,2,3]
x = solve.permutations(n1)


def generatePermutations(nums):
    answers = []

    permutation = []
    used = set()

    def backtrack():
        if (len(permutation) == len(nums)):
            answers.append(permutation.copy())
            return
        #[1, 2, 3]
        # N * (N * N-1 ...1 )= N*N!
        # depth = N  
        for i in range(len(nums)):
            if i not in used:
                used.add(i)
                permutation.append(nums[i])
                backtrack()
                used.remove(i) # 2 
                permutation.pop() # nums[2] == 3 

    backtrack()
    return answers