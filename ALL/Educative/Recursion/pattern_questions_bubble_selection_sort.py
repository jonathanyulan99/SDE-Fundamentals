'''
Q: Print This Pattern
    * * * * 
    * * *
    * *
    * 
'''

def pattern_1(row:int,col:int)->None:
    # we are at the bottom of our pattern 
    # base case end 
    if row == 0:  
        return 
    
    
    if row > col:
        print('*',end=' ') 
        pattern_1(row,col+1)
        
    else:
        print() 
        pattern_1(row-1,0)  

pattern_1(4,0) 

'''
Q: Print This Pattern
    * 
    * *
    * * *
    * * * * 
'''

def pattern_2(row:int,col:int)->None:
    # we are at the bottom of our pattern 
    # base case end 
    if row == 0:  
        return 
    
    
    if row > col:
        pattern_2(row,col+1)
        print('*',end=' ') 
        
    else:
        pattern_2(row-1,0) 
        print() 
        
pattern_2(4,0) 

def bubble_sort_recursively(arr:list[int],r:int,c:int):
    if r == 0:
        return
    
    if c < r: 
        if arr[c] > arr[c+1]:
            arr[c],arr[c+1] = arr[c+1],arr[c]
        bubble_sort_recursively(arr,r,c+1)
    else:
        bubble_sort_recursively(arr,r-1,0)

t = [4,3,2,1]
print(f'\n{t}') 
bubble_sort_recursively(t,len(t)-1,0)
print(t)

'''
Q:  Selection Sort 
    Takes Largest Element in the List and swap it with the last Element 
    Takes Second Largest Element in the List and swap it with the second to last element 
    
    [4,3,2,8,1] * 8 largest element 
    [4,3,2,1,8] * 4 largets element 
    [1,3,2,4,8] * 3 largest element 
    [1,2,3,4,8] ** sorted * 2 largest element 
'''

def selection_sort_recursively(arr:list[int],row:int,col:int,max_index:int):
    if row == 0:
        return 
    
    if col<row:
        if arr[col] > arr[max_index]:
            selection_sort_recursively(arr,row,col+1,col)
        else:
            selection_sort_recursively(arr,row,col+1,max_index)        
    else:
        arr[max_index],arr[row-1] = arr[row-1],arr[max_index] 
        selection_sort_recursively(arr,row-1,0,0)

x = [5,4,1,3,2]
selection_sort_recursively(x,len(x),0,0)
print(x)

