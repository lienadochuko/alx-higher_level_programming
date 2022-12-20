#!/usr/bin/python3
"""Define a class square."""


class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current square area."""
        x=self.__size * self.__size
        return (x)
        