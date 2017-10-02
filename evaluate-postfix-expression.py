# Given a postfix expression, the task is to evaluate the expression and
# print the final value.

# Input:
# The first line of input will contains an integer T denoting the no of
# test cases . Then T test cases follow. Each test case contains an
# postfix expression.

# Output:
# For each test case, evaluate the postfix expression and print the value.

# Constraints:
# 1 <= T <= 100
# 1 <= length of expression <= 100

# Example:

# Input:
# 2
# 231*+9-
# 123+*8-

# Output:
# -4
# -3
# code
# Stack Functions to be used by printNGE()

import re


def createStack():
    stack = []
    return stack


def isEmpty(stack):
    return len(stack) == 0


def push(stack, x):
    stack.append(x)


def pop(stack):
    if isEmpty(stack):
        print("Error : stack underflow")
    else:
        return stack.pop()


def evaluate_postfix_expression(input):
    stk = createStack()
    for i in input:
        isNum = re.match('\d', i)
        isSymbol = re.match('[+*-/]', i)
        if isNum:
            push(stk, i)
        elif isSymbol:
            secondOperand = pop(stk)
            firstOperand = pop(stk)
            if i == '+':
                push(stk, (int(firstOperand) + int(secondOperand)))
            if i == '-':
                push(stk, (int(firstOperand) - int(secondOperand)))
            if i == '*':
                push(stk, (int(firstOperand) * int(secondOperand)))
            if i == '/':
                push(stk, (int(firstOperand) / int(secondOperand)))
    print pop(stk)

if __name__=='__main__':
    #print(t)
    t = input()
    for i in range(int(t)):        
        arr = str(raw_input())
        evaluate_postfix_expression(arr)
        

