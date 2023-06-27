#!/usr/bin/python3

class Square:
    """
    Represents a square.

    Attributes:
        side_length (int): The side length of the square.
    """

    def __init__(self, side_length=0):
        """
        Initialize a new square.

        Args:
            side_length (int): The side length of the square. Default is 0.

        Raises:
            TypeError: If side_length is not an integer.
            ValueError: If side_length is less than 0.
        """
        if not isinstance(side_length, int):
            raise TypeError("Side length must be an integer")
        elif side_length < 0:
            raise ValueError("Side length must be >= 0")
        self.__side_length = side_length

    def get_side_length(self):
        """
        Get the side length of the square.

        Returns:
            int: The side length of the square.
        """
        return self.__side_length

    def set_side_length(self, value):
        """
        Set the side length of the square.

        Args:
            value (int): The new side length value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("Side length must be an integer")
        elif value < 0:
            raise ValueError("Side length must be >= 0")
        self.__side_length = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__side_length ** 2

    side_length = property(get_side_length, set_side_length)
