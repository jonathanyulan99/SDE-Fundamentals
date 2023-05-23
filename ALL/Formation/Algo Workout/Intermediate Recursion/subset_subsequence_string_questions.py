'''
Q: Find if an Array is sorted or not? 
    Input: arr = [1,2,4,8,9,12]
    output = True 
'''
def return_sorted(lst:list[int])->bool:
    answer = True 
    if lst:
        def helper(lst,start):
            if len(lst) == (start + 1):
                return True 
            # if lst[start] <= lst[start+1]:
            #     return helper(lst,start+1)
            # else:
            #     return False 
            return lst[start] <= lst[start+1] and helper(lst,start+1)
        answer = helper(lst,0)
    return answer 

print(return_sorted([1,4,2,8,9,12]))

'''
original input: 'baccaad'
return output: 'bccd'

Given a string get rid of all the 'A's into the string 
'''
string_input = 'baacaaddd'

def remove_a(string:str)->str:
    if string:
        def helper(string,index,answer):
            if len(string) == index:
                    return answer

            if string[index] == 'a':
                return helper(string,index+1,answer)
            return helper(string,index+1,answer+string[index])
        return helper(string,0,'')
    else:
        return string

print(remove_a(string_input)) 

def remove_a_two(string:str, index:int=0,subsequnce:str ='')->str:
    if len(string)==index:
        return subsequnce
    
    character = string[index]
    
    if character == 'a':
        return remove_a_two(string,index+1,subsequnce)
    return remove_a_two(string,index+1,subsequnce+character)

print(remove_a_two('baccaddda'))

'''
Subset & Subsequence Problems 
    * Permutations & Combinations 
    * Subsets -> Non-Adjacent Collection & Non-Continuous & Continuous Elements 
        [3,5,9] -> [3],[3,5],[3,9],[3,5,9],[5,3,9],[5,3],[5],[9] 
        * Create All The Subsets of a `Collection`
            * str = 'abc'
            * ouput = ['a','b','c','ab','ac','bc','abc','acb']
            * ORDERING CANNOT CHANGE 
            * ['ab'] == ['ba'] 
            * This pattern of taking some elements & removing some is known as the SUBSET PATTERN
            * subsequence = '' ; processed = 'abc' 
            * A pattern of taking an element of the string or not taking that element 
'''

def subset_generation(sequence:str):
    output = [] 
    def subset_generation_helper(sequence,subsequence,index):
        if len(sequence) == index:
            output.append(subsequence)
            return 
        
        subset_generation_helper(sequence,subsequence+sequence[index],index+1)
        subset_generation_helper(sequence,subsequence+str(ord(sequence[index])),index+1)
        subset_generation_helper(sequence,subsequence,index+1)
        
        
    subset_generation_helper(sequence,'',0)
    return output 

print(subset_generation('abc'))

def subset_duplicates(sequence:list[int])->list[list[int]]:
    sequence.sort() 
    # if current & previous element is same, start = end + 1 
    outer = [[]]
    start = 0 
    end = 0
    for i in range(len(sequence)):
        start = 0 
        if i > 0 and sequence[i] == sequence[i-1]:
            start = end + 1 
        end = len(outer) - 1 
        internal = [] 
        for j in range(start,len(outer)):
            internal = outer[j].copy()
            internal.append(sequence[i])
            outer.append(internal)
    return outer 

arr = [1,2,2]

def main():
    ans = subset_duplicates(arr)
    for x in ans:
        print(x) 

main()

