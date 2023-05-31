'''
                                            Merge Sort 
                                        
                                        arr = [8,3,4,12,5,6]
        left_arr = [8,3,4]                                                  right_arr = [12,5,6]
        ..
        ....
..recursive calls 
        ....
        .. 
        left_arr = [3,4,8]                                                  right_arr = [5,6,12]
                            Then On The Way Back We Are Going To Merge Back 
                            
            (8,3,4)
        (8,3)       (4)* single element is the base condition
    (8)     (3)* the single element is already sorted 
    
        (3,8)       (4)
            
            (3,4,8)
                            
STEPS:
    1) Divide Array into Two Parts 
    2) Get Both Parts Sorted Via Recursion 
    3) Merge The Sorted Parts 
    
    Deeper Explanation: arr1 = [3,5,9]
                        arr2 = [4,6,8] ** Moving pointers from the arrays you grab, if there were more elements still leftover just .extend the rest of the iterable to the newly sorted list 
                        
                        [3,4,5,6,8,9]
'''

def merge_sort(inp:list[int])->list[int]: 
    # base condition
    if len(inp)==1:
        return inp 
    
    middle = len(inp)//2
    
    # this is not done in place we are using slicing thus utilizing a great deal of memory 
    left = merge_sort(inp[:middle])
    right = merge_sort(inp[middle:]) 
    
    def merge(first,second):
        output = [] 
        i,j = 0,0 
        
        while i < len(first) and j < len(second):
            if first[i] < second[j]: 
                output.append(first[i])
                i+=1 
            else:
                output.append(second[j])
                j+=1 
        
        output.extend(first[i:])
        output.extend(second[j:])
        return output
    
    return merge(left,right) 

import random 
arr = [random.randrange(1,100) for x in range(0,10)]
print(arr)
arr = merge_sort(arr) 
print(arr) 

def merge_sort_in_place(inp:list[int],start:int,end:int)->None:
    if end-start == 1:
        return
    
    middle = (start + end) // 2 

    merge_sort_in_place(inp,start,middle) 
    merge_sort_in_place(inp,middle,end) 
    
    def merge_in_place(inp,start,middle,end):
        output = []
        i = start 
        j = middle 
        k = 0
        
        while i < middle and j < end:
            if inp[i] < inp[j]:
                output.append(inp[i])
                i+=1 
            else:
                output.append(inp[j])
                j+=1 
        
        # Copy remaining elements from the first half, if any
        #output.extend(inp[i:middle])

        # Copy remaining elements from the second half, if any
        #output.extend(inp[j:end])
         
        while i < middle:
            output.append(inp[i])
            i+=1  
            
        while j < end:
            output.append(inp[j])
            j+=1  
            
        for i in range(len(output)):
            inp[start+i] = output[i]
    
    merge_in_place(inp,start,middle,end)
    
arr = [random.randrange(1,100) for x in range(0,10)]
print(arr)
merge_sort_in_place(arr,0,len(arr))
print(arr) 

nums = [1,2,3,4,5,6]
middle = len(nums)//2 

print(nums[:middle])
print(nums[middle:])