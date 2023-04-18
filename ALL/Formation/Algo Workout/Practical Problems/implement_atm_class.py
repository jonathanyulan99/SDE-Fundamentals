'''
❓ PROMPT
You are asked to write a program that simulates an ATM machine. 
The program should allow users to perform the following operations:

1. Check balance: Display the current balance of the user's account.
2. Deposit: Add money to the user's account.
3. Withdraw: Remove money from the user's account, if sufficient funds are available.

The program should have the following features:
- The program should be able to handle multiple user accounts.
- The program should store account balances persistently (i.e., in memory).
- The program should allow the user to specify the amount of money to deposit or withdraw.
- The program should validate user input and handle errors gracefully (e.g., invalid input, insufficient funds).
- The program should return appropriate messages to the user after each operation.

ATM Class Definition

- create_account(initial_balance) -> int: \
    Creates a new account with an optional initial balance and returns the account ID.
    
- get_balance(account_id) -> float: \
    Returns the balance of the account with the specified ID, or None if the account is not found.
    
- deposit(account_id, amount) -> str: \
    Deposits the specified amount of money into the account with the specified ID and
    returns a string message describing the deposit. If the deposit is successful,
    the message should be in the following format:
        "Deposit successful. Your new balance is $<balance>.". 
    If the deposit fails due to an error, the message should be in the following format:
        "Deposit failed: Account not found."
- withdraw(account_id, amount) -> str: 
    Withdraws the specified amount of money from the account with the specified ID and returns a string 
    message describing the withdrawal. If the withdrawal is successful, the message should be in the following 
    format: 
        "Withdrawal successful. Your new balance is $<balance>.". If the withdrawal fails due to an error, 
    the message should be in one of the following formats:
        "Withdrawal failed: Account not found."
        "Withdrawal failed: Insufficient funds."

Example(s)
atm = ATM()

# Create some accounts
account1 = atm.create_account()
account2 = atm.create_account(100.0)
account3 = atm.create_account(50.0)

# Deposit and withdraw money
print(atm.deposit(account1, 50.0))  # should print "Deposit successful. Your new balance is $50.00."
print(atm.withdraw(account1, 20.0))  # should print "Withdrawal successful. Your new balance is $30.00."
print(atm.withdraw(account1, 40.0))  # should print "Withdrawal failed: Insufficient funds."

🛠️ IMPLEMENT
class ATM:
    def __init__(self):
        self.accounts = {}

    def create_account(self, initial_balance=0.0) -> int:
        pass

    def get_balance(self, account_id: int) -> Optional[float]:
        pass

    def deposit(self, account_id: int, amount: float) -> str:
        pass

    def withdraw(self, account_id: int, amount: float) -> str:
        pass
        
- deposit(account_id, amount) -> str: \
    Deposits the specified amount of money into the account with the specified ID and
    returns a string message describing the deposit. If the deposit is successful,
    the message should be in the following format:
        "Deposit successful. Your new balance is $<balance>.". 
    If the deposit fails due to an error, the message should be in the following format:
        "Deposit failed: Account not found."
- withdraw(account_id, amount) -> str: 
    Withdraws the specified amount of money from the account with the specified ID and returns a string 
    message describing the withdrawal. If the withdrawal is successful, the message should be in the following 
    format: 
        "Withdrawal successful. Your new balance is $<balance>.". If the withdrawal fails due to an error, 
    the message should be in one of the following formats:
        "Withdrawal failed: Account not found."
        "Withdrawal failed: Insufficient funds."
'''
class ATM(object):
    def __init__(self):
        self.accounts = {} 
        self.accountID = 1
        
    def create_account(self, initial_balance=00.00) -> int:
        self.accounts[self.accountID] = initial_balance  
        # you need to save accountID prior to sending it back because we are consistently sending back the new updated ID
        accountID = self.accountID
        self.accountID += 1 
        return accountID

    def get_balance(self, account_id: int) -> float:
        if account_id in self.accounts: 
            return f'{float(self.accounts[account_id])}'
        else:
            return None 

    def deposit(self, account_id: int, amount: float) -> str:
        if account_id in self.accounts: 
            self.accounts[account_id] += amount
            return f"Deposit successful. Your new balance is ${self.accounts[account_id]:.2f}"
        else: 
            return f'Deposit failed: Account not found.'

    def withdraw(self, account_id: int, amount: float) -> str:
        if account_id in self.accounts: 
            if amount <= self.accounts[account_id]:
                self.accounts[account_id] -= amount
                return f'Withdrawal successful. Your new balance is ${self.accounts[account_id]:.2f}'
            else: 
                return f'Withdrawal failed. Insufficient funds.'
        else:
            return f'Withdrawal failed: Account not found.'

atm = ATM() 

# Create some accounts
account1 = atm.create_account()
account2 = atm.create_account(100.0)
account3 = atm.create_account(50.0)

# # Deposit and withdraw money
# print(atm.deposit(account1, 50.0))  # should print "Deposit successful. Your new balance is $50.00."
# print(atm.withdraw(account1, 20.0))  # should print "Withdrawal successful. Your new balance is $30.00."
# print(atm.withdraw(account1, 40.0))  # should print "Withdrawal failed: Insufficient funds."

def test_atm():
    atm = ATM()

    # Test creating accounts
    assert atm.create_account() == 1
    assert atm.create_account(100.0) == 2
    assert atm.create_account(50.0) == 3

    # Test depositing and withdrawing money
    print(atm.deposit(1, 50.0))# == 'Deposit successful. Your new balance is $50.00'
    print(atm.get_balance(1)) #== 50.0
    print(atm.withdraw(1, 20.0))# == 'Withdrawal successful. Your new balance is $30.00'
    print(atm.withdraw(1, 40.0))# == 'Withdrawal failed. Insufficient funds.'
    print(atm.get_balance(1))# == 30.0

    # Test handling invalid account IDs
    print(atm.get_balance(4))# None
    print(atm.deposit(4, 100.0)) #== 'Account not found'
    print(atm.withdraw(4, 50.0)) #== 'Account not found'
    print('Tests passed')

test_atm()