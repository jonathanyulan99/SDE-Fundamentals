def move_zeroes(nums):
    last_non_zero_index = 0 
    for idx in range(len(nums)):
        if nums[idx] != 0:
            nums[last_non_zero_index] = nums[idx]
            last_non_zero_index += 1
    
    for idx in range(last_non_zero_index,len(nums)):
        nums[idx] = 0 
    
    '''
            slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            # wait while we find a non-zero element to
            # swap with you
            if nums[slow] != 0:
                slow += 1
    '''

n = [0,1,0,3,12]

move_zeroes(n) 