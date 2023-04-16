def produce(upperBound:int):
    primes = [] 
    
    for i in range(0,upperBound+1):
        primes.append(tuple((i,True)))
    
    primes[0] = tuple([0,False])
    primes[1] = tuple([1,False])
    
    for i in range(2,upperBound+1):
        if True in primes[i]:
            j = 2 
            while j*i <= upperBound:
                primes[j*i] = tuple([(i*j),False])
                j += 1 
            
    result = [] 
    for i in range(len(primes)):
        if True in primes[i]:
            result.append(i)
    
    return result

prime_list = produce(1000)
print(prime_list)