#!/usr/bin/python3
for num in range(ord('z'), ord('a')-1, -1):
    if num % 2 == 1:
        num -= 32
    print("{:c}".format(num), end='')
