
'''
❓ PROMPT
The [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) is an ancient algorithm 
for finding all of the prime numbers between up to a given upper bound. It's much more efficient than a function 
to check whether or not a given single number is prime, if that function is going to be called many times.

The way it works is quite straight foward: We start by assuming all of the numbers between two and 
the upper bound are prime. Then starting from two, if that number is still marked as prime, we then 
start counting by twos and remove all of it's multiples. Then move on to three. When we get to four, 
we've already removed it from our set of candidates, so we continue to five. Five has not been removed 
so is prime, now count by fives and remove all of those numbers.

This is often implemented with an array of booleans and they all start out as true, 
then we mark the composites as false, but it makes a lot of sense to do this with a set, 
first filling it with all of the candidates and then removing the composites.

Example(s)
sieveOfEratosthenes(5) => 2, 3, 5
sieveOfEratosthenes(10) => 2, 3, 5, 7
 

🔎 EXPLORE
List your assumptions & discoveries:
 

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
function sieveOfEratosthenes(upperBound)
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
import math


def sieve_of_eratosthenes(nums: int) -> list:
    primes = set()

    for x in range(2, nums+1):
        primes.add(x)

    # bound = math.sqrt(nums)

    # for x in range(2, math.ceil(bound)):
    #     if x in primes:
    #         for num in range(x+x, nums+1, x):
    #             primes.remove(num)

    # return primes
    return_container = set()
    while primes:
        start_prime_two = min(primes)
        if start_prime_two in primes:
            return_container.add(start_prime_two)
            primes = primes.difference(
                set(range(start_prime_two, nums+1, start_prime_two)))

    return return_container


print(sieve_of_eratosthenes(100))
