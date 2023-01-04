#!/usr/bin/python3
"""Define say_my_name function"""


def say_my_name(first_name, last_name=""):
    """Print name.

    Args:
        first_name(str): First name to be printed.
        last_name(str): Last name to be printed.
    Raise:
        TypeError: If the name are not strings.
    Print:
        My name is <first_name> <last_name>.
    """

    if (not isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    if (not isinstance(last_name, str)):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
