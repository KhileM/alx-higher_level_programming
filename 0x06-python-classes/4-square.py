#!/usr/bin/python3

class Square:
    def __init__(self, side_length=0):
        if not isinstance(side_length, int):
            raise TypeError("Side length must be an integer")
        elif side_length < 0:
            raise ValueError("Side length must be >= 0")
        self.__side_length = side_length

    def get_side_length(self):
        return self.__side_length

    def set_side_length(self, value):
        if not isinstance(value, int):
            raise TypeError("Side length must be an integer")
        elif value < 0:
            raise ValueError("Side length must be >= 0")
        self.__side_length = value

    def area(self):
        return self.__side_length ** 2

    side_length = property(get_side_length, set_side_length)
