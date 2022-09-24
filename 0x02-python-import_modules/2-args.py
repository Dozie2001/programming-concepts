#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    len_arg = len(argv)
    if len_arg == 1:
        print("{} argument.".format(len_arg - 1))
    elif len_arg == 2:
        print("{} argument:".format(len_arg - 1))
    else:
        print("{} arguments:".format(len_arg - 1))
    for i in range(1, len_arg):
        print("{}: {}".format(i, argv[i]))
