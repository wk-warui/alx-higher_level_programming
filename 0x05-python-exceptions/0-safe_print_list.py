#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    n = 0
    if x == 0:
        print()
        return n
    try:
        for n in range(x):
            print(my_list[n], end="")
            print()
    except IndexError:
        print()
        return n
    return n + 1
