nums = [1,2,3,4,5]
# slice(start,stop_not_including,increment)
# very similiar if not the same as [start:stop:increment]
nums_2 = nums[slice(0,len(nums),2)]
print(nums_2)
nums_slice = nums[slice(len(nums))]
print(nums_slice)