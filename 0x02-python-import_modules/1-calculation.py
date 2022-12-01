#!/usr/bin/python3

if __name__ == "__main__":

    """import functions from file"""
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5
print("result: {} + {} = {}".format(a, b, add(a, b))) """addition function"""
print("result: {} - {} = {}".format(a, b, sub(a, b))) """subtraction function"""
print("result: {} * {} = {}".format(a, b, mul(a, b))) """multiplication function"""
print("result: {} / {} = {}".format(a, b, div(a, b))) """division function"""

