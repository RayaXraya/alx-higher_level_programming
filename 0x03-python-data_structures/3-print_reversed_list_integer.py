#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    "prints integers of a list in reverse"
    if not my_list:
        return None
    for i in reversed(my_list):
        print("{:d}".format(i)
