'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different 
day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''

def maximum_profit(prices:list[int])->int:
    result = 0 
    l = 0 
    
    for r in range(len(prices)):
        if prices[l] < prices[r]:
            result = max(result,prices[r]-prices[l])
        else:
            l = r 

    return result 

print(maximum_profit([7,1,5,3,6,4]))
print(maximum_profit([7,6,4,3,1]))