#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, div, mul
    ft = "{:d} {} {:d} = {:d}"

    if not len(argv[1:]) == 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    o = argv[2]
    if o == '+':
        print(ft.format(a, o, b, add(a, b)))
    elif o == '-':
        print(ft.format(a, o, b, sub(a, b)))
    elif o == '*':
        print(ft.format(a, o, b, mul(a, b)))
    elif o == '/':
        print(ft.format(a, o, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
