#!/usr/bin/python3

if __name__ == "__main__":
    """addition"""
    from add_0 import add

    a = 1
    b = 2
    c = add(a, b)
    print("{} + {} = {}".format(a, b, add(a, b)))
