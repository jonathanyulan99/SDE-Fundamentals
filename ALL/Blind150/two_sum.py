'''
Q:  Given an array of integers 'nums' and an integer 'target', return indices of the two numbers such that they add up to 'target'. 
        You May Assume that each input would have exactly one solution, and you may not use the same element twice
            You can Return the answer in any order 
'''
class Solution(object):
    def two_sum(self,nums:list[int],target:int)->list[int]:
        # will always have an answer 
        num_complements = {} 
        
        for idx, num in enumerate(nums): 
            print(target-num)
            if num_complements.get((target-num),'A')!='A':
                return [num_complements[target-num],idx]
            else:
                num_complements[num] = idx 

nums1 = [2,7,11,15]
target = 9 
# return [0,1]

nums1 = [3,2,4] 
target = 6
# returns [1,2] 

nums1 = [3,3] 
target = 6 
# returns [0,1]

solve = Solution()
print(solve.two_sum(nums1,target))
            