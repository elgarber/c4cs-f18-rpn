#!/usr/bin/env python3
import operator

op = {
        '+': operator.add, 
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.floordiv,
}

def calculate(arg):
    # Stack for calculator
    stack = []
    tokens = arg.split()

    # process tokens 
    for token in tokens:
        try:
            value = int(token)
            stack.append(value)
        
        except ValueError:
            val2 = int(stack.pop())
            val1 = int(stack.pop())

            #look up function in operation table
            func = op[token]
            result = func(val1, val2)
            stack.append(str(result))
    
    return int(stack[0])
    

def main():
    while True:
        print (calculate(input('rpn calc>')))
        

if __name__ == '__main__':
        main()

