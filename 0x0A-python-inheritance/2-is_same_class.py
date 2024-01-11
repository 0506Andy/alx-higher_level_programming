#!/usr/bin/python3
"""Defines the class checking function."""


def is_same_class(obj, a_class):
    """Check if the  object is the exact  instance of the given class.

    Args:
        obj (any): The object that we check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an exact instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
