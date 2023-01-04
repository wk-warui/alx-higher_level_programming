#!/usr/bin/python3
"""Define print_square function"""


def print_square(size):
    """ Pint a square with character #.

    Args:
        size: The size length of the square.
    Raise:
        TypeError: If size is not an integer
        ValueError: If size < 0
        TypeError: if size is a float and is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if is(size, float) and is(size < 0):
        raise TypeError("size must be an integer")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
