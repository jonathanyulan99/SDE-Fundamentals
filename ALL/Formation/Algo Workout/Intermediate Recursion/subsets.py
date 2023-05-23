from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        if nums:
            def helper(nums,subseq,result):
                result.append(subseq)
                
                for i in range(len(nums)):
                    helper(nums[i+1:],subseq+[nums[i]],result)

            helper(nums,[],result)
        return result
    
class Solution:
    def subsets(self,nums:List[int])->list[list[int]]:
        result = []
        
        subsets = [] 
        def dfs(ind:int):
            if ind == len(nums):
                result.append(subsets.copy())
                return 
            
            subsets.append(nums[ind])
            dfs(ind + 1)
            # backtrack and don't include
            subsets.pop() 
            dfs(ind + 1)
        dfs(0)
        return result 
    
subsets = Solution()
nums = [1,2,3]
print(subsets.subsets(nums))