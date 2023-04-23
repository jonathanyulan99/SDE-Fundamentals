'''
Tax Calculator

You are given a list of tax brackets, where each bracket is defined by a range of taxable income and a marginal tax rate. Your task is to write a function that takes in a taxable income and returns the amount of tax payable on that income based on the given tax brackets.

Write a function `calculate_tax(taxable_income: float, brackets: List[Tuple[float, float, float]]) -> float` that takes the following parameters:

`taxable_income`: a float representing the amount of taxable income
`brackets`: a list of tuples, where each tuple contains three floats: the lower limit of the bracket (exclusive), the upper limit of the bracket (inclusive), and the marginal tax rate for that bracket. The first tuple should represent the lowest bracket and have a lower limit of 0 and an upper limit greater than 0.

The function should return the total amount of tax payable on the taxable_income, calculated as the sum of the tax payable for each bracket.

[Optional]: How would you account for deductions? What about tax credits?

Further reading: https://www.nerdwallet.com/article/taxes/federal-income-tax-brackets
 

EXAMPLE(S)
If the taxable income is $80,000 and the tax brackets are:
`[(0, 10000, 0.10), (10000, 30000, 0.15), (30000, 60000, 0.25), (60000, float('inf'), 0.35)]`

The function should return 18500, which is calculated as follows:

The first $10,000 is taxed at 10%, which is $1,000
The next $20,000 is taxed at 15%, which is $3,000
The next $30,000 is taxed at 25%, which is $7,500
The remaining $20,000 is taxed at 35%, which is $7,000
The total tax payable is $1,000 + $3,000 + $7,500 + $7,000 = $18,500
 

FUNCTION SIGNATURE
`def calculate_tax(taxable_income: float, brackets: List[Tuple[float, float, float]]) -> float`
'''
# Deductions can reduce the amount of your income before you calculate the tax you owe. 
# Credits can reduce the amount of tax you owe or increase your tax refund.
def calculate_tax(taxable_income: float, brackets: list[tuple[float, float, float]],deductions:float=0,tax_credits:float=0) -> float:
    taxable_income -= deductions 
    owed_taxes = 0 
    
    for lower,upper,rate in brackets:
        diff = min(upper,taxable_income) - lower 
        if diff > 0:
            diff_rate = diff * rate 
            owed_taxes += diff_rate
        else:
            break
    
    result_num = round(owed_taxes - tax_credits,2)
    return result_num if result_num >= 0 else f'You are owed {-1*result_num}'

print(calculate_tax(80000,[(0,10000,0.10),(10000,30000,0.15),(30000,60000,0.25),(60000,float('inf'),0.35)],tax_credits=20000))
import unittest
class TestCalculateTax(unittest.TestCase):
    def test_single_bracket(self):
        brackets = [(0, 10000, 0.10)]
        self.assertAlmostEqual(calculate_tax(5000, brackets), 500, places=2)
        self.assertAlmostEqual(calculate_tax(10000, brackets), 1000, places=2)
        self.assertAlmostEqual(calculate_tax(15000, brackets), 1000, places=2)
    
    def test_multiple_brackets(self):
        brackets = [
            (0, 10000, 0.10),
            (10000, 30000, 0.15),
            (30000, 60000, 0.25),
            (60000, float('inf'), 0.35),
        ]
        self.assertAlmostEqual(calculate_tax(5000, brackets), 500, places=2)
        self.assertAlmostEqual(calculate_tax(15000, brackets), 1750, places=2)
        self.assertAlmostEqual(calculate_tax(35000, brackets), 5250, places=2)
        self.assertAlmostEqual(calculate_tax(80000, brackets), 18500, places=2)
    
    def test_large_bracket(self):
        brackets = [(0, float('inf'), 0.10)]
        self.assertAlmostEqual(calculate_tax(50000, brackets), 5000, places=2)
        self.assertAlmostEqual(calculate_tax(100000, brackets), 10000, places=2)
        self.assertAlmostEqual(calculate_tax(150000, brackets), 15000, places=2)
    
    def test_empty_brackets(self):
        brackets = []
        self.assertAlmostEqual(calculate_tax(50000, brackets), 0, places=2)

if __name__ == '__main__':
  unittest.main()

print(calculate_tax(80000,[(0,10000,0.10),(10000,30000,0.15),(30000,60000,0.25),(60000,float('inf'),0.35)],0,15000))
