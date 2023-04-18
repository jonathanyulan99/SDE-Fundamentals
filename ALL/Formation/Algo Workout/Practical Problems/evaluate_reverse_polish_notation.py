'''
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.

'''
def evaluate_rpn(tokens: list[str]) -> int:
    stack = [] 
    
    for token in tokens:
        if token not in ['*','/','+','-']:
            stack.append(int(token))
        else: 
            operand_two = stack.pop()
            operand_one = stack.pop() 
            
            if token == '+':
                result = operand_one + operand_two
            elif token == '*':
                result = operand_one * operand_two 
            elif token == '-':
                result = operand_one - operand_two 
            else:
                result = int(float(operand_one)/operand_two)
            stack.append(result)
    
    return stack.pop() 
