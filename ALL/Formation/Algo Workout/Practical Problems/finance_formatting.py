'''
❓ PROMPT
You're working on a finance application and need to format monetary amounts in the following manner for accounting purposes. Every number must adhere to a strict set of rules:

1. All amounts are rounded to two decimal places, even if it is .00.
2. A $ precedes the first digit.
3. Thousands, millions, billions, etc have commas between every 3 digits from the left of the decimal.
4. Negative numbers are surrounded by parentheses.
5. If the absolute amount is less than 1, there should still be a zero before the '.'

Write a function that takes a numeric value and outputs the "finance formatted" string representation.

This is a very realistic data processing problem with lots of special cases!

Example(s)
moneyFormat(0) == "$0.00"
moneyFormat(1) == "$1.00"
moneyFormat(-1) == "($1.00)"
moneyFormat(16) == "$16.00"
moneyFormat(123) == "$123.00"
moneyFormat(123123) == "$123,123.00"

P:
    amount: float number must be outputted to a string adhering to specific rules 
    negative nunbers are handled differently than positive intially but then follow the same rules 
    if the *amount* goes past or equals the .00X then just output $0.00
    if '.' not in the *amount* then we need to add .00 
    if there is a '.' then we don't need to add .00 but we need to add a '$0' in the beginning
    check for negative if there is add (*amount*) then continue to format
    if the length of the amount is greater than 3 then we need to add ',' (maybe input from the end of the *amount* in this case)
  
    instantiate str ending and beginning $ and .00
    check for the amount if it's a negative then we need to add '(' to the beginning and close at the end of our formatting with a ')' 
    
    Handle negatives as a special case. Detect this at the beginning and then format it at the end
    Get the decimal portion by multiplying by 100 then mod by 100.
    Get the integer portion by dividing by 100 and taking the floor.
    
    Add commas by looping while the value is greater than zero. Mod 1000 to get the next section of digits then divide by 1000 to shift everything else over. Store these parts in an array.
    Format the decimal part and each part in the array to have leading zeros if needed.
    Combine the results at the end and decorate negative numbers.
  
  
'''
def moneyFormat(amount: float) -> str:
    
    def pad_zeroes(number:int,length:int):
        new_zeroes = length - len(str(number))
        return ''.join(['0'] * new_zeroes) + str(number) 
    
    # check for negative numbers intially for later formatting 
    # how you can get around for instantiating and then setting for the value 
    # instead of is_negative = initial_value
    # if condiitonal_statement: is_negative = new_value or stays the same due to boolean type, 2 choices 
    is_negative = amount < 0
    
    amount = -amount if is_negative else amount 
    
    # take the amount times it by 100 to move the last two values after the decimal point to before the decimal 
    # then take the mod of 100 instead of 10 which would be the digit and grab the hundread and tens place
    # (amount * 100) % 100 
    amount = round(amount*100)
    decimalPart = pad_zeroes(amount%100,2)
    # get the integer portion by dividing by 100 and taking the floor 
    # can do this with math.floor() or with // 
    amount = amount//100 
    
    # if our number is > 999 then we need to add commas 
    # we will loop while the value is greater than 0 
    comma_num_parts = []
    while amount > 0:
        # % 1000 here cuts off the ones,tens and hundreads digigts and leaves the thousands 
        # 9999 % 1000 = 999
        # 9999//1000 = 9 
        # 1231234
        section = amount % 1000
        comma_num_parts.append(str(section))
        amount = amount // 1000 
    # we need to reverse our comma_num_parts sections 
    # 1231234 
    # our comma_num_parts looks like 234 231 1 
    # in our [0] spot in our array is 234 we want it listed 1 231 234 
    comma_num_parts.reverse() 
    
    for i in range(1,len(comma_num_parts)):
        # never have to add leading zeroes to the first number here 
        # thus is why we start at 1 
        comma_num_parts[i] = pad_zeroes(comma_num_parts[i],3)
        
    # special case when the amount is less than 1 
    if len(comma_num_parts) == 0:
        comma_num_parts.append('0')
    
    # takes our long list of number parts and joins them with a comma after the 1st portion 
    dollar_portion = ','.join(comma_num_parts)
    final_amount = f'${dollar_portion}.{decimalPart}'
    
    return f'({final_amount})' if is_negative else final_amount

# happy cases
print(moneyFormat(0) == "$0.00")
print(moneyFormat(1) == "$1.00")
print(moneyFormat(-1) == "($1.00)")
print(moneyFormat(16) == "$16.00")
print(moneyFormat(123) == "$123.00")

# decimal variants
print(moneyFormat(0.01) == "$0.01")
print(moneyFormat(.02) == "$0.02")
print(moneyFormat(.3) == "$0.30")
print(moneyFormat(0.0001) == "$0.00")
print(moneyFormat(4.954) == "$4.95")
print(moneyFormat(4.955) == "$4.96")
print(moneyFormat(4.) == "$4.00")

# comma variants
print(moneyFormat(1234) == "$1,234.00")
print(moneyFormat(1001.01) == "$1,001.01")
print(moneyFormat(50000) == "$50,000.00")
print(moneyFormat(6789123456789) == "$6,789,123,456,789.00") # 6.7 trillion

# negative variants
print(moneyFormat(-0.01) == "($0.01)")
print(moneyFormat(-.02) == "($0.02)")
print(moneyFormat(-0.001) == "($0.00)")
print(moneyFormat(-1000) == "($1,000.00)")

# complex variants
print(moneyFormat(-34567) ==  "($34,567.00)")
print(moneyFormat(-12345.67) ==  "($12,345.67)")
print(moneyFormat(-12345.678) ==  "($12,345.68)")