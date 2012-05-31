"""
Module containing logic concerning mutation
"""
import random
from bitstring import Bitstring, flip_positions

random_object = random.Random()


def mutate(value):
    if isinstance(value, int):
        return shift_by_one(value)
    elif isinstance(value, Bitstring):
        return shift_by_bit(value)
    else:
        raise TypeError("mutate function called on unknown type")


def shift_by_bit(bitstring):
    return flip_positions(bitstring, [random_object.randrange(len(bitstring))])


def shift_by_one(num):
    """
    returns the increment or decrement (randomly) of a number
    """
    shift = random_object.randrange(-1, 3, 2)
    return num + shift
