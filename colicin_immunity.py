"""
a colicin is represented by a single number
immunity is represented by another number
colicin binding to immunity is represented by the
abs-difference being less than
a threshold
"""
import random
from mixins import Duplicatable, Printable, Equalable


class Colicin(Duplicatable, Printable, Equalable):

    def __init__(self, id):
        self.id = id

    def duplicate(self):
        duplicate = Colicin(self.id)
        return duplicate

    def mutate(self):
        """
        Returns a Colicin with an id shifted by one
        """
        new_id = shift_by_one(self.id)
        return Colicin(new_id)


class Immunity(Duplicatable, Printable, Equalable):
    def __init__(self, id, binding_range):
        self.id = id
        self.binding_range = binding_range

    #0 or immunity objects- pass a colicin (ask can you bind!)

    def can_bind(self, colicin):
        dif = colicin.id - self.id
        abs_dif = abs(dif)
        return abs_dif <= self.binding_range

    def mutate(self):
        """
        Returns an immunity instance shifted by one
        (Binding range unchanged)
        """
        return Immunity(shift_by_one(self.id), self.binding_range)


def shift_by_one(num):
    """
    returns the increment or decrement (randomly) of a number
    """
    shift = random.randrange(-1, 3, 2)
    return num + shift
