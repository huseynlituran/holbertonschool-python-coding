#!/usr/bin/python3
"""Module that defines a Square class with size property and area method."""


class Square:
    """Square class with a private size attribute."""

    def __init__(self, size=0):
        """Initialize square with size using the size setter."""
        self.size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with type and value validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size
