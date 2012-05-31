"""
Module containing logic concerning mutation
"""
import random

random_object = random.Random()

def mutate(value):
    if isinstance(value, int):
        return shift_by_one(value)

def shift_by_one(num):
    """
    returns the increment or decrement (randomly) of a number
    """
    shift = random_object.randrange(-1, 3, 2)
    return num + shift
