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