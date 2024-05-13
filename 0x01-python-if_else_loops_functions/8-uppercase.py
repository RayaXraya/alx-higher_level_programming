#!/usr/bin/python3
# Author - Rayan

def islower(c):
    """Checks for lowercase"""
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False


def uppercase(str):
    """turn into upper case letter"""
    for i in str:
        print("{:c}"
              .format(ord(i) if not islower(i) else ord(i) - 32),
              end="")
    print("")
