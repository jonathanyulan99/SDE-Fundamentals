def is_sorted_recursively(inp:list[int])->bool:
    '''
    Q: Find If An Array is Sorted or Not 

    arr = [1,2,4,8,9,12] *sorted*
    arr = [1,2,4,3,8,9] *not sorted*

    arr[ previous_index || current_index -1 ] < arr[ previous_index+1 || current_index ]
    arr[i] < arr[i+1] 
    Your stopping condition is when the array index is out of bounds, or when the array has been completely traversed 
    (1,2,4,8,9,12)
    is 1 < 2 and continue(4,8,9,12)
                        is 4 < 8 and continue(9,12)
                                            9< 12 and continue(12) 
                                                            END OF ARRAY return True 
    ** if at any point the arr[i] IS NOT < arr[i+1] then return False 
    '''
    if not inp:
        return True 
    def helper(inp,start):
        # base condition 
        # index == arr.length - 1 
        if start == len(inp) - 1:
            return True 
        # will never go out of bounds due to the start variable condition 
        return inp[start] < inp[start+1] and helper(inp,start+1)
        
    return helper(inp,0) 

print(is_sorted_recursively([1,2,4,8,9,12]))
    

def return_linear_search_bool(inp:list[int],target:int)->bool: 
    '''
    Q: Given An Array return whether that item exist or not? 
    Return the Index or Position or Boolean Value   
    '''
    if inp and target:
        def helper(inp,target,start):
            if start == len(inp):
                return -1
            if inp[start] == target:
                return start 
            return helper(inp,target,start+1) 
        return helper(inp,target,0)
    return inp 

test = [1,2,3,4,5,6,7,8]
target = 9

print(f'index for {target} is: {return_linear_search_bool(test,target)}')
print(f'position for {target} is: {return_linear_search_bool(test,target)}')
# weird interaction 
print(False+0,False + 1,True+0,True+1)

def return_linear_search_bool_from_back_of_array(inp:list[int],target:int)->bool: 
    '''
    Q: Given An Array return whether that item exist or not? 
    Return the Index or Position or Boolean Value   
    '''
    if inp and target:
        def helper(inp,target,start):
            if start < 0:
                return -1
            if inp[start] == target:
                return start 
            return helper(inp,target,start-1) 
        return helper(inp,target,len(inp)-1)
    return inp 

test = [1,2,3,4,5,6,7,8]
target = 8


print(f'index for {target} is: {return_linear_search_bool_from_back_of_array(test,target)}')
print(f'position for {target} is: {return_linear_search_bool_from_back_of_array(test,target)+1}')

def return_list_of_indexes(inp:list[int],target)->list[int]:
    container = [] 
    if inp:
        def helper(inp,target,start):
            if len(inp) == start:
                return
            if inp[start] == target:
                container.append(start)
            helper(inp,target,start+1)
        helper(inp,target,0)
    return container

test = [2,4,3,1,4,4,5]
target = 4 

print(return_list_of_indexes(test,target))

# if you do not want to use scope in order to pass the array/container/list then we can pass it as a parameter and now return the list 
# every function call has different reference variables but they all are pointed to the same object 
# value is being added in the original value 
def return_list_of_indexes_v2(inp:list[int],target,container=[])->list[int]:
    if inp:
        def helper(inp,target,start):
            if len(inp) == start:
                return
            if inp[start] == target:
                container.append(start)
            helper(inp,target,start+1)
        helper(inp,target,0)
    return container if container else -1 

test = [4,2,4,3,1,4,4,5]
target = 4

print(return_list_of_indexes_v2(test,target))

'''
Q: Return the List of All Indexes but do not take it as a parameter as an arguement 
    create it in the body of the function 
    Why is this challenging? Because each recrusive call will have it own instance of a list associated with it, 
                             every call will have a new list, so we need a way to traverse the returned data to the above function
                             and eventually the main function original call 
                             
    [1,2,3,4,4,8],target=4,start_index=0 
    (arr,target,0) 
        {list=[]} 
        (arr,target,1)
            {list=[]}
            (arr,target,2)
                {list=[]}
                (arr,target,3)
                    {list=[3]} ** only available in this function call 
                    (arr,target,4)
                        {list=[4]} ** only avaiable in this function call 
                        (arr,target,5) 
                            {list=[]}
                                (arr,target,6)
                                    {list=[]} ****BASE CONDITION NOW RETURNING BACK 
    # if you just return the list at the end of this recursive calls, then you will just a return an empty list 
    # you need to take the answers at each recursive calls, so you need to do something at the end of the function calls 
                      
'''

def return_list_of_indexes_v3(inp:list[int],target)->list[int]:
    if inp and target:
        def helper(inp,target,start):
            # not very optimized because you make containers/list for every recursive call frame 
            container = []
            # local list created
            if start == len(inp):
                return container 
            
            # this will contain answer for that function call only 
            # note that each recrusive stack call frame will have its own containers of answers 
            if inp[start] == target: 
                container.append(start) 
            
            # answers from below calls 
            # this is going to be tied to container because the base case is a list that is getting returned 
            answers_from_below = helper(inp,target,start+1) 
            
            # extending is taking an iterable and then returning the rest of the answers from below 
            container.extend(answers_from_below) 
            return container 
            
        return helper(inp,target,0)
    else:
        return None 
    
arr = [1,2,2,3,4,4,5,6,4]
target = 4 

print(return_list_of_indexes_v3(arr,target))

'''
Q: Rotated Binary Search
indexes:       0 1 2 3 4 5 6 7 
arr:          [5,6,7,8,9,1,2,3] 
search/target:           7
 
'''

def rotated_binary_search(inp:list[int],target:int,start:int,end:int)->list[int]:
    if start > end:
        return -1 
    
    middle = (start + (end-start)) // 2 
    
    # our first check to see if our middle_index is the target 
    if inp[middle] == target:
        return middle 
    
    # is the first element of the recursive call frame smaller than the middle element 
    if inp[start] <= inp[middle]:
        
        # We now that this portion is sorted 
        # Check to see if the target lives in this range 
        # Target lives in the sorted beginning portion of the array 
        if target >= inp[start] and target <= inp[middle]:
            
            # change our ending point to the middle - 1 
            return rotated_binary_search(inp,target,start,middle-1)
        else:
            
            # it lies outsisde this window then 
            # so set the start to middle + 1 
            return rotated_binary_search(inp,target,middle+1,end)
    
    # This gets executed if the beginning isn't sorted 
    # check to see if our target lives in that unsorted/sorted portion outside 
    if target >= inp[middle] and target <= inp[end]:
        return rotated_binary_search(inp,target,middle+1,end)
    
    return rotated_binary_search(inp,target,start,middle-1)

test = [4,5,6,1,2,3]
print(rotated_binary_search(test,6,0,len(test)-1))