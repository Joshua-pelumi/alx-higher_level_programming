#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div
if __name__ == '__main__':
    if len(argv) != 4:
        print(f'Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)

    op = argv[2]
    a = int(argv[1])
    b = int(argv[3])
    result = 0
    if op == '+':
        result = add(a, b)
    elif op == '-':
        result = sub(a, b)
    elif op == '*':
        result = mul(a, b)
    elif op == '/':
        result = div(a, b)
    else:
        print(f'Unknown operator. Available operators: +, -, * and /')
        exit(1)

    print(f'{a} {op} {b} = {result}')
