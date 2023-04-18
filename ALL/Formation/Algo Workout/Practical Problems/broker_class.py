class CryptoBroker:
    def __init__(self, deposits):
        self.users = [{"cash": deposit, "crypto": 0} for deposit in deposits]

    def deposit(self, user_id, amount):
        self.users[user_id - 1]["cash"] += amount

    def buy(self, user_id, amount, price):
        user = self.users[user_id - 1]
        cost = amount * price
        if cost > user["cash"]:
            raise ValueError("Not enough cash to buy")
        user["cash"] -= cost
        user["crypto"] += amount

    def sell(self, user_id, amount, price):
        user = self.users[user_id - 1]
        if amount > user["crypto"]:
            raise ValueError("Not enough crypto to sell")
        user["crypto"] -= amount
        user["cash"] += amount * price

    def get_balance(self, user_id):
        return self.users[user_id - 1]["cash"]

def solution(deposits, operations):
    broker = CryptoBroker(deposits)
    result = []
    for op in operations:
        tokens = op.split()
        if tokens[0] == "deposit":
            broker.deposit(int(tokens[1]), int(tokens[2]))
        elif tokens[0] == "buy":
            broker.buy(int(tokens[1]), int(tokens[2]), int(tokens[3]))
        elif tokens[0] == "sell":
            broker.sell(int(tokens[1]), int(tokens[2]), int(tokens[3]))
        result.append(broker.get_balance(int(tokens[1])))
    return result

def solution(deposits, operations):
    users = [{"cash": deposit, "crypto": 0} for deposit in deposits]
    result = []
    for op in operations:
        tokens = op.split()
        if tokens[0] == "deposit":
            user_id, amount = int(tokens[1]), int(tokens[2])
            users[user_id - 1]["cash"] += amount
        elif tokens[0] == "buy":
            user_id, amount, price = int(tokens[1]), int(tokens[2]), int(tokens[3])
            #user = users[user_id - 1]
            cost = amount * price
            if cost <= users[user_id-1]["cash"]:
                users[user_id -1]["cash"] -= cost
                users[user_id-1]["crypto"] += amount
        elif tokens[0] == "sell":
            user_id, amount, price = int(tokens[1]), int(tokens[2]), int(tokens[3])
            #user = users[user_id - 1]
            if amount <= users[user_id-1]["crypto"]:
                users[user_id-1]["crypto"] -= amount
                users[user_id-1]["cash"] += amount * price
        result.append(users[int(tokens[1]) - 1]["cash"])
    return result

'''
Implement a simplified version of a crypto broker platform. Initially, there is an array of users, with each user depositing only cash - deposits[i] is the
amount of cash the (i + 1)th user has deposited.
Assume that for now the platform contains just a single stock and all operations are done with this stock only. 
All operations are supposed to be in the same currency, and currency exchange is not supported for now.

The platform should support the following 3 types of operations:

"deposit <user_id> <amount>" - deposits money to the specified user account.

"buy <user_id> <amount> <price>" - the specified user buys the specified amount of crypto at the specified price. 
The platform should make sure the user has enough money in their account to process the operation.

"sell <user_id> <amount> <price>" - the specified user sells the specified amount of crypto at specified price. 
The platform should make sure the user has enough cryptos in their account to process the operation.
Note that in all operations, user_id is a 1-based identifier.

Your task is to return an integer array representing the total amount of money in the specified user's account after each operation.

Example

For deposits = [9, 7, 12] and

operations = [
  "buy 1 3 2",
  "sell 1 4 10",
  "deposit 2 12",
  "buy 2 10 2",
  "buy 2 6 3"
]
the output should be solution(deposits, operations) = [3, 3, 19, 19, 1].

Let's consider all operations:

The user with user_id = 1 wants to buy 3 shares of the stock at price = 2 - the required amount of money is needed_money = 3 * 2 = 6. 
    The user has 9 ≥ 6 units of money in their account, so this operation will be processed successfully. After this operation, the user has 3 units of money remaining.
    
The user with user_id = 1 wants to sell 4 shares of the stock at price = 10 - this operation will not be processed successfully because the user does not have 4 shares of the stock.
    Since the operation is not processed successfully, the user still has 3 units of money remaining.
    
The user with user_id = 2 deposits 12 units of money into their account. After this operation, the user has 19 units of money.

The user with user_id = 2 wants to buy 10 shares the stock at price = 2 - the required amount of money is needed_money = 10 * 2 = 20.
    The user has 19 < 20 units of money in their account, so this operation will not be processed successfully. The user still has 19 units of money remaining.
    
The user with user_id = 2 wants to buy 6 shares of the stock at price = 3 - the required amount of money is needed_money = 6 * 3 = 18. 
    The user has 19 ≥ 18units of money, so this operation will be processed successfully. After this operation, the user has 1 unit of money remaining.
    
So, the output is [3, 3, 19, 19, 1].

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer deposits

An array of integers representing the amount of money (in cash) that users deposit to their accounts.

Guaranteed constraints:
1 ≤ deposits.length ≤ 104,
1 ≤ deposits[i] ≤ 105.

[input] array.string operations

An array of strings representing the operations described above. Specifically, it's guaranteed that:

In buy and sell operations - amount and price are integers.
In all operations - user_id will be integers between 1 to deposits.length, amount will be integers between 1 to 20000, price will be integers between 1 to 105.
After each operation, the total amount of money in each user's account will be an integer.
Guaranteed constraints:
1 ≤ operations.length ≤ 104.

[output] array.integer

An array of integers where the ith element of the array represents the total amount of money in the specified user's account after the ith operation.
'''
def solution(deposits:list[int],operations:list[str])->list[int]:
    users = [{'cash':deposit, 'shares':0}for deposit in deposits]
    output = list()
    for operation in operations:
        op = operation.split()
        action = op[0] 
        user_id = int(op[1])
        if action == "deposit":
            users[user_id-1]['cash'] += int(op[2])
        elif action == "buy":
            shares,price = int(op[2]),int(op[3])
            share_price = shares * price 
            if users[user_id-1]['cash'] >= share_price:
                users[user_id-1]['cash'] -= share_price  
                users[user_id-1]['shares'] += shares 
        elif action == "sell":
            selling_shares = int(op[2])
            shares = users[user_id-1]['shares']
            if shares >= selling_shares:
                sell_share_price = int(op[2]) * int(op[3])
                users[user_id-1]['cash'] += sell_share_price 
                users[user_id-1]['shares'] -= selling_shares 
        output.append(users[user_id-1]['cash'])
    return output 

d = [9, 7, 12] 
operations = [
  "buy 1 3 2",
  "sell 1 4 10",
  "deposit 2 12",
  "buy 2 10 2",
  "buy 2 6 3"
]

print(solution(d,operations))
# Test case 1
deposits = [10, 20, 30]
operations = ["buy 1 5 2", "deposit 2 10", "buy 3 10 3"]
assert solution(deposits, operations) == [0, 30, 0]


# Test case 2
deposits = [100, 50, 75]
operations = ["buy 1 25 4", "sell 2 10 6", "buy 3 10 3"]
assert solution(deposits, operations) == [0, 50, 45]
