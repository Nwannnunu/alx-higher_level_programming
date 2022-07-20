#!/usr/bin/python3
"""private instance attribute"""


class Square(object):
    """class Variable size"""
    def __init__(self, size):
        """initialize size"""
        self.__size = size
