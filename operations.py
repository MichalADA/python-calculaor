import math
import PySimpleGUI as sg



def shunting_yard(input_string):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, 's': 4}
    op_stack = []
    output = []
    i = 0
    while i < len(input_string):
        if input_string[i].isdigit():
            j = i
            while j < len(input_string) and input_string[j].isdigit():
                j += 1
            output.append(int(input_string[i:j]))
            i = j
        elif input_string[i] in precedence:
            while op_stack and op_stack[-1] != '(' and precedence[input_string[i]] <= precedence[op_stack[-1]]:
                output.append(op_stack.pop())
            op_stack.append(input_string[i])
            i += 1
        elif input_string[i] == '(':
            op_stack.append(input_string[i])
            i += 1
        elif input_string[i] == ')':
            while op_stack and op_stack[-1] != '(':
                output.append(op_stack.pop())
            if op_stack and op_stack[-1] == '(':
                op_stack.pop()
            i += 1
        else:
            i += 1
    while op_stack:
        output.append(op_stack.pop())
    return output




def evaluate_rpn(tokens):
    stack = []
    for token in tokens:
        if type(token) is int:
            stack.append(token)
        else:
            if token == '+':
                if len(stack) >= 2:
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a + b)
            elif token == '-':
                if len(stack) >= 2:
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a - b)
            elif token == '*':
                if len(stack) >= 2:
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a * b)
            elif token == '/':
                if len(stack) >= 2:
                    b = stack.pop()
                    a = stack.pop()
                    if b == 0:
                        return "BŁĄD nie można dzielić przez zero"
                    stack.append(a // b)
            elif token == '^':
                if len(stack) >= 2:
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a ** b)
            elif token == 's':
                if len(stack) >= 1:
                    a = stack.pop()
                    if a < 0:
                        return "BŁĄD"
                    stack.append(math.sqrt(a))
    return stack[0]





def calculate(input_string):
    tokens = shunting_yard(input_string)
    return evaluate_rpn(tokens)




def to_binary(value):
    return bin(int(value))


def to_hex(value):
    return hex(int(value))


def to_oct(value):
    return oct(int(value))


def to_dec(value):
    return int(value ,0 )
