#!/usr/bin/env python3
import operator

op = {
        '+': operator.add, 
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.floordiv,
        '^': operator.ipow,
        '&': operator.and_,
        '|': operator.or_,
        'xor' : operator.ixor,

}

def rotate(l, n):
    return l[n:] + l[:n]

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
            if(token == "rl"):
                stack = rotate(stack, 1)
            else:
                val2 = int(stack.pop())
                val1 = int(stack.pop())
                 
                func = op[token]
                result = func(val1, val2)
                stack.append(str(result))
    
    return int(stack[0])
    

def main():
    while True:
        print (calculate(input('rpn calc>')))
        

if __name__ == '__main__':
        main()

