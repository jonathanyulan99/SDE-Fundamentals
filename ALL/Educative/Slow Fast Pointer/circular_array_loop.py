'''
An input array, nums containing non-zero integers, is given, where the value at each index 
represents the number of places to skip forward (if the value is positive) or backward 
(if the value is negative). When skipping forward or backward, wrap around if you reach either end of the array.
For this reason, we are calling it a circular array. Determine if this circular array has a cycle. 
A cycle is a sequence of indices in the circular array characterized by the following:
    1.The same set of indices is repeated when the sequence is traversed in accordance with the aforementioned rules.
    2.The length of the sequence is at least two.
    3.The loop must be in a single direction, forward or backward.
'''
def is_circular_array(nums:list[int])->bool:
    forward = True 
    # [-2, -3, 1, -3, 2]
    #   S          
    #   F
    S = 0 
    F = 0 
    
    for index in range(1,len(nums)):
        prev = S 
        S = next_step(S,nums[S],len(nums))
        if is_not_cycle(nums,prev,S):
            F,S = index,index 
            continue 
        
        next_iteration = False 
        fast_moves = 2 
        
        for _ in range(fast_moves):
            prev = F 
            fast = next_step(F,nums[F],len(nums))
            if is_not_cycle(nums,prev,F):
                fast,slow = index,index 
                next_iteration = True 
                break 
        
        if next_iteration:
            continue 
        
        if slow == fast:
            return True 
        
    return False 
        
def next_step(slow_pointer_value,arr_value,size):
    # this means the values can be 0,1,..size-1 
    # [0,1,...size-1]
    # keeps our array in bounds 
    result = (slow_pointer_value + arr_value) % size 
    if result < 0:
        result = size + result 
    return result 

def is_not_cycle(arr,prev_value,slow_value):
    if (arr[prev_value]>=0 and arr[slow_value]<0) or abs(arr[prev_value]%arr[slow_value])==0:
        return True 
    else:
        return False 
