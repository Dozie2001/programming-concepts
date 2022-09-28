#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    len_list = len(my_list) - 1
    count = -1
    for i in range(len(my_list) - 1, -1, -1):
        print("{:d}".format(my_list[i]))