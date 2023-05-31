'''
                                                    QuickSort
                                                    
                                            {10,80,30,90,40,50,70}
                                * partation around pivot, usually last element here its 70
                            {10,30,40,50}                           {90,80}
                    {10,30,40}            {}                    {}          {90}
                {10,30}       {}
            {10}     {}
'''
def quicksort(inp:list[int],start_index,end_index)->None:
    if start_index >= end_index:
        return 

    i = start_index 
    j = end_index 
    # middle = (start_index + end_index)//2 
    # this is utilziing the middle_index and the below utilizes the end_index 
    pivot = inp[end_index]
    
    while i <= j: 
        # this is why this sorting method is used more in practice due to the fact that there may not be any moving indices 
        # works very well for pre-sorted data 
        while inp[i] < pivot: 
            i+=1 
        
        while inp[j] > pivot:
            j-=1 
        
        if i <= j: 
            inp[i],inp[j] = inp[j],inp[i]
            i+=1 
            j-=1 
    
    quicksort(inp,start_index,j) 
    quicksort(inp,i,end_index) 
    
import random 
test = [random.randint(0,1000)for x in range(10)]
print(test)
quicksort(test,0,len(test)-1)
print(test) 