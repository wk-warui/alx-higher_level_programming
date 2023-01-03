#!/usr/bin/python3
"""Define class Rectangle"""


class Rectangle:
    """Represent a rectangle"""

    def __init__(self, width=0 height=0):
        """Initialize a new rectangle.

        Args:
            width (int): width of the new rectangle
            height (int): height of the new rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self.__height

    @width.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Get the area of the rectangle(height * width)"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Get the perimeter of the rectangle((height * 2) + (width * 2))"""
        if self.__width == 0 or self.height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
