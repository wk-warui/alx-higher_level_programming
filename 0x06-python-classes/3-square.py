#!/usr/bin/python3

"""Defines a class Square"""


class Square:
    """Represents a Square"""
    def __init__(self, size):
        """Initializing a sqaure.

        Args:
            size (int): Size of the new square)
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current area of the square"""
        return (self.__size * self.__size)
