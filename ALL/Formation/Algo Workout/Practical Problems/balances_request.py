def solution(balances, requests):
    for i, request in enumerate(requests, 1):
        orders = request.split()
        if orders[0] == 'withdraw':
            from_account = int(orders[1])
            amount = int(orders[2])
            if from_account <= 0 or from_account > len(balances):
                return [-i]
            if amount > balances[from_account-1]:
                return [-i]
            balances[from_account-1] -= amount 
        elif orders[0] == 'transfer':
            from_account = int(orders[1])
            to_account = int(orders[2]) 
            amount = int(orders[3])
            if from_account <= 0 or from_account > len(balances) or to_account <= 0 or to_account > len(balances):
                return [-i]
            if amount > balances[from_account-1]:
                return [-i]
            balances[from_account-1] -= amount 
            balances[to_account-1] += amount
        elif orders[0] == 'deposit':
            to_account = int(orders[1])
            amount = int(orders[2])
            if to_account <= 0 or to_account > len(balances):
                return [-i]
            balances[to_account-1] += amount
    return balances

def solution(balances,requests):
    request_number = -1
    for request in requests: 
        orders = request.split()
        if orders[0] == 'withdraw':
            from_account = int(orders[1])
            amount = int(orders[2])
            if from_account <= 0 or from_account > len(balances):
                return [request_number]
            if amount >= balances[from_account-1]:
                return [request_number] 
            else:
                balances[from_account-1] -= amount 
        elif orders[0] == 'transfer':
            from_account = int(orders[1])
            to_account = int(orders[2]) 
            amount = int(orders[3])
            if balances[from_account-1] < amount: 
                return [request_number] 
            elif from_account <= 0 or from_account > len(balances):
                return [request_number]
            elif to_account <= 0 or to_account > len(balances):
                return [request_number] 
            else: 
                balances[from_account-1] -= amount 
                balances[to_account-1] += amount
        elif orders[0] == 'deposit':
            to_account = int(orders[1])
            amount = int(orders[2])
            if to_account <= 0 or to_account > len(balances):
                return [request_number]
            else:
                balances[to_account-1] += amount
        request_number -= 1 
    return balances 