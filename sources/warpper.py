"""Wrapper modul for library "libmatheDynLib.dylib"
This is a warpper for an external library written in C.
The library offers two functions:
1. double CircleArea (double radius)
2. double PowerOf2 (double number)
"""
from ctypes import *


mydll = cdll.LoadLibrary("lib/libmatheDynLib.dylib")


def circle_area(number):
    """Calculates circle area

    :param number: Radius
    :type number: any
    :return: Circle area value
    :rtype: float
    """
    value = convert_to_float(number)
    __circle_area = mydll.CircleArea
    __circle_area.argtypes = [c_double]
    __circle_area.restype = c_double

    return __circle_area(value)


def power_of_2(number):
    """Calculates power of 2

    :param number: Number
    :type number: any
    :return: Result of power of 2
    :rtype: float
    """
    value = convert_to_float(number)
    __power_of_2 = mydll.PowerOf2
    __power_of_2.argtypes = [c_double]
    __power_of_2.restype = c_double

    return __power_of_2(value)


def convert_to_float(number):
    """Convert given parameter to float

    :param number: Parameter to convert
    :type number: any
    :raises Exception: ValueError
    :return: Number
    :rtype: float
    """
    try:
        value = float(number)
    except ValueError as err:
        raise Exception(err)

    return value
