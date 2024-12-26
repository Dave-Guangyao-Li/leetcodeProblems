'''
valuating a basic mathematical expression string with +, -, *, and / operations

If the input string includes parentheses (e.g., "3+(2*2)"), we need to handle nested expressions. This requires adjusting the algorithm to evaluate the parentheses first, as they take the highest precedence in arithmetic expressions.

'''


'''
Operations * and / have higher precedence than + and -.
We’ll need to handle operators and numbers in order while respecting precedence.

Use a stack to store intermediate results.
Traverse the string character by character:
	•	If the character is a digit, accumulate it (to handle multi-digit numbers).
	•	If the character is an operator or the end of the string:
	•	For * and /, pop the last number from the stack, perform the operation, and push the result back.
	•	For + and -, push the number with its sign onto the stack.
•	Sum up the stack at the end for the final result.



1.	When encountering an open parenthesis (, push the current result and operator onto the stack, and reset the current result.
	2.	When encountering a closing parenthesis ), pop the last result and operator from the stack and combine them with the current result.
	3.	The rest of the logic remains the same as the basic calculator (handling +, -, *, /).
'''


def calculate(s: str) -> int:
    # Step 1: Initialize variables
    stack = []  # To hold intermediate results and operators
    num = 0     # Current number being processed
    operator = '+'  # Default operator
    result = 0  # Running result

    # Step 2: Iterate over the characters in the string
    for i, char in enumerate(s):
        # If the character is a digit, build the number
        if char.isdigit():
            # build multi-digit numbers from individual characters in the input string.
            num = num * 10 + int(char)

        # If the character is an operator, a parenthesis, or end of string
        if char in "+-*/()" or i == len(s) - 1:
            if char == '(':
                # Push the current result and operator to the stack
                stack.append(result)
                stack.append(operator)
                # Reset result and operator for the new sub-expression
                result = 0
                operator = '+'
            elif char == ')':
                # Apply the last operator to the current number
                if operator == '+':
                    result += num
                elif operator == '-':
                    result -= num
                elif operator == '*':
                    result *= num
                elif operator == '/':
                    result = int(result / num)

                # Pop operator and previous result from the stack
                operator = stack.pop()
                prev_result = stack.pop()
                # Combine with the previous result
                if operator == '+':
                    result = prev_result + result
                elif operator == '-':
                    result = prev_result - result

                # Reset num
                num = 0
            else:
                # Apply the previous operator before moving to the next
                if operator == '+':
                    result += num
                elif operator == '-':
                    result -= num
                elif operator == '*':
                    result *= num
                elif operator == '/':
                    result = int(result / num)

                # Update the operator
                operator = char
                num = 0

    return result


# print(calculate("(3+2)*2"))
print(calculate("(10+2)*3-(6/2)"))  # 33
print(calculate("10+(2*3)-(6/2)"))  # 13

'''

When parsing a string like "123+45", we need to handle multi-digit numbers such as 123 and 45 because the input is processed one character at a time.

Example:

	1.	First, you encounter '1', then '2', then '3'.
	2.	To combine these into the number 123, you can’t just take each character independently.
	3.	Instead, you build the number progressively:
	•	num = 1
	•	num = 1 * 10 + 2 = 12
	•	num = 12 * 10 + 3 = 123
 
 

s = "10+(2*3)-(6/2)"
Expected Output:

Evaluate the expression:
	1.	2 * 3 = 6
	2.	6 / 2 = 3
	3.	10 + 6 - 3 = 13

Output: 13


Initialization:

	•	stack = [] (to save results and operators for parentheses)
	•	result = 0 (running total)
	•	num = 0 (current number being processed)
	•	operator = '+' (default operator)
 
 Step-by-Step Execution:

	1.	Process '1':
	•	num = 1.
	2.	Process '0':
	•	num = num * 10 + int('0') = 10.
	3.	Process '+':
	•	Apply operator ('+') to result: result = result + num = 0 + 10 = 10
 Reset num = 0, update operator = '+'.
    4.	Process '(':
	•	Push result = 10 and operator = '+' onto the stack:
        stack = [10, '+']
        
    
    Reset result = 0, operator = '+'.
    5.	Process '2':
	•	num = 2.
	6.	Process '*':
	•	Apply operator ('+') to result:result = result + num = 0 + 2 = 2
 	Reset num = 0, update operator = '*'.
    7.	Process '3':
	•	num = 3.
	8.	Process ')':
	•	Apply operator ('*') to result: result = result * num = 2 * 3 = 6
    •	Pop operator ('+') and prev_result (10) from the stack:
        result = prev_result + result = 10 + 6 = 16
        stack = []
    	•	Reset num = 0.
    9.	Process '-':
        •	Apply operator ('+') to result: result = result + num = 16 + 0 = 16 •	Reset num = 0, update operator = '-'.
    10.	Process '(':
	    •	Push result = 16 and operator = '-' onto the stack: stack = [16, '-'] 	•	Reset result = 0, operator = '+'.
    11.	Process '6':
	    •	num = 6.
	12.	Process '/':
	    •	Apply operator ('+') to result:
        result = result + num = 0 + 6 = 6
        Reset num = 0, update operator = '/'.
    13.	Process '2':
	    •	num = 2.
	14.	Process ')':
	    •	Apply operator ('/') to result: result = int(result / num) = int(6 / 2) = 3
        •	Pop operator ('-') and prev_result (16) from the stack:
            result = prev_result - result = 16 - 3 = 13
            stack = []
result = 13
'''
