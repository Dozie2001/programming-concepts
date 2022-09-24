#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    len_arg = len(argv)
    if len_arg == 1:
        print(f"{len_arg - 1} argument")
    elif len_arg == 2:
        print(f"{len_arg - 1} argument:")
    else:
        print(f"{len_arg - 1} arguments:")
    for i in range(1, len_arg):
        print(f"{i}: {argv[i]}")
