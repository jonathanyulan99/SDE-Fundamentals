def gcd(num1:int,num2:int)->int:
    def helper(num1,num2,count=1):
        if count > num1 or count > num2:
            return count
        
        count = helper(num1,num2,count+1)
        if num1 % count == 0 and num2 % count == 0:
            return count 
        else:
            return count - 1
    
    return helper(num1,num2)

#Without the Use of A Helper Function
def gcd(num1:int,num2:int)->int:
    if num1 == num2:
        return num1 
    
    if num1 > num2:
        return gcd(num1-num2,num2)
    else:
        return gcd(num1,num2-num1)


print(gcd(15,5)==5)
print(gcd(56,42)==14)
print(gcd(42,56)==14)
print(gcd(14,30)==2)
print(gcd(27,13)==1)
print(gcd(23,23)==23)
