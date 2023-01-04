#!/usr/bin/python
"""Defines an integer addition function"""


def add_integer(a, b=98):
    """Return the sum of a and b.

        Float arguments are typecasted to integers before addition is
    performed.

        Raises:
            TypeError: if a or b is not an Integer/Float.
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
        return (int(a) + int(b))
