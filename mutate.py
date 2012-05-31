"""
Module containing logic concerning mutation
"""
import random

random_object = random.Random()

def shift_by_one(num):
    """
    returns the increment or decrement (randomly) of a number
    """
    shift = random_object.randrange(-1, 3, 2)
    return num + shift
