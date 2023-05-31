'''
Q:  You Are Climbing A Staircase. It takes 'n' steps to reach the top.

    Each time you can climb 1 or 2 steps. In how many distinct ways can you reach the top?
'''
dp = {}
dp[1] = 1
dp[2] = 2
def solve(n:int)->int:
    if n in dp:
        return dp.get(n)
    
    return solve(n-1) + solve(n-2) 

print(solve(2))