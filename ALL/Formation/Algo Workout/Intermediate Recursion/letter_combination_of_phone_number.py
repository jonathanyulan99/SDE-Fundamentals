
'''
Mapping Numbers to Possible Combinations

1:abc
2:def
3:ghi
4:jkl 
5:mno
6:prq
7:stu
8:vwx
9:yz

input: '12'
possible_outputs: ad,ae,af,bd,be,bf,
using unprocessed/processed method 

                        "1 2" 
    {pro}/{unpro}      
        a/2         b/2         c/2     
    
ab/'' ae/'' af/''            
*unprocessed == 0/empty base case 
*unprocessed is our original list 
'''
class Solution(object):
    def solve(input:str)->None:
        if input:
            def helper(pro,unp):
                if len(unp)==0:
                    print(pro)
                    return 
                
                # convert the string to an int 
                digit = int(unp[0])
                
                # go from [(digit-1) *3 , 3)
                # 
                for i in range((digit-1)*3,digit*3):
                    character_to_add = chr(ord('a') + i) 
                    helper(pro+character_to_add,unp[1:])
            helper('',input)
        return [] 

class Solution(object):
    def solve(input:str)->list[str]:
        if input:
            def helper(pro,unp):
                if len(unp)==0:
                    returned_list = [] 
                    returned_list.append(pro[:])
                    return returned_list 
                
                # convert the string to an int 
                digit = int(unp[0])
                output = [] 
                # go from [(digit-1) *3 , 3)
                # 
                for i in range((digit-1)*3,digit*3):
                    character_to_add = chr(ord('a') + i) 
                    # .allAll(the_recursive_list_returned_back) 
                    output.extend(helper(pro+character_to_add,unp[1:]))
                return output 
                    
            return helper('',input)
        else:
            return [] 
    
solve = Solution
print(solve.solve('34'))