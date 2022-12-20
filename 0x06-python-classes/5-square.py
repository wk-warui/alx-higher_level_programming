#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """Represents a square."""
    def __init__(self, size=0):
        """Initialize the square.


        Args:
            size (int): new size of the square.
        """
        self.__size = size

    @property
    def size(self):
        """retrieves the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """set the size of the square."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints the square with the # character."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
                print("")
