#!/usr/bin/pythone

"""Define a class Square"""


class Square:
    """Represemts a square"""
    def __init__(self, size):
        """Initialize a square.


        Args:
            size (init): Size of the new squar.
        """
        self.__size = size

    @property
    def size(self):
        """Get the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)
