# if a number is divided by a divisor it can give divisor-1 different numbers
# if the divsor is 4 then the modulus can be 0,1,2,3 but never 4 because 4/4 = 1 r 0 
# remainder is the modulus factor we are going for 
def modulus_of(dividend:int,divisor:int)->int:
    if divisor == 0:
        print('Cannot Divide By Zero')
        return float('-inf')
    
    if dividend < divisor:
        return dividend 
    
    return modulus_of(dividend-divisor,divisor)

print(modulus_of(12,3)==0)
print(modulus_of(12,5)==2)
print(modulus_of(12,7)==5)
