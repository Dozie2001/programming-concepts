#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    len_args = len(argv) - 1

    result = 0
    for i in range(1, len_args + 1):
        result += int(argv[i])
    print(result)
