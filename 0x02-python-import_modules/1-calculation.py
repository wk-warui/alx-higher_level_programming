#!/usr/bin/python3

if __name__ == "__main__":

    """import functions from file"""
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5
print("{} + {} = {}".format(a, b, add(a, b))) """addition function"""
print("{} - {} = {}".format(a, b, sub(a, b))) """subtraction function"""
print("{} * {} = {}".format(a, b, mul(a, b))) """multiplication function"""
print("{} / {} = {}".format(a, b, div(a, b))) """division function"""

