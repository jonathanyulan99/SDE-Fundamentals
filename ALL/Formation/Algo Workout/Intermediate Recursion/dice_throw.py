'''

Given a Target: 4 
Given Data Type [1,2,3,4,5,6] => 6 sided die 
Find all the Combinations of all the Target  
4 => [4,1111,22,31]
                       {unp}/{pro}
                           0/4
        1/3     2/2                 3/1     4/0 **Base Case Hit 
    12/1 13/0 21/1 22/0          31/0 
1111/0 121/0
'''
class Solution(object):
    def solve(inp:int):
        if inp:
            def helper(unp,pro):
                if pro == 0:
                    print(unp) 
                    return
                
                for i in range(1,6):
                    if i <= pro:
                        helper(unp+str(i),pro-i)
            helper('',inp)
        return []

class Solution(object):
    def solve(inp:int,die_face:int)->list[int]:
        if inp:
            def helper(unp,pro):
                if pro == 0:
                    returned_list = []
                    returned_list.append(int(unp))
                    return returned_list
                
                output = [] 
                for i in range(1,die_face+1):
                    if i <= pro:
                        output.extend(helper(unp+str(i),pro-i))
                return output 
            return helper('',inp)
        return []

solve = Solution
print(solve.solve(4,6))

                    