# 10 9 8 7 6 5 4 3 2 1 
# 10 5 2 1 
def find_factors(n:int,a=1,container=[])->list[int]:
    if a > n: 
        return container
    
    if n % a == 0:
        container.append(a) 
    
    return find_factors(n,a+1,container)

print(find_factors(100))