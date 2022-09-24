#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, div, mul, sub
    len_args = len(argv) - 1

    if len_args == 3:
        a = int(argv[1])
        b = int(argv[3])
    else:
        exit(1)

    if argv[2] == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
        exit(0)

    elif argv[2] == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
        exit(0)
    elif argv[2] == '/':
        print("{} / {} = {}".format(a, b, div(a, b)))
        exit(0)

    elif argv[2] == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
        exit(0)
    else:
        print("Unkown operator. Available operators: +, -, * and /")
        exit(1)
