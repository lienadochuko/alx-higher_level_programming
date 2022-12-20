#!/usr/bin/python3
"""Define a class square."""


class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """retrieve the current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return (self.__size * self.__size)
