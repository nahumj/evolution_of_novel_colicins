"""
a colicin is represented by a single number
immunity is represented by another number
colicin binding to immunity is represented by the
abs-difference being less than
a threshold
"""
import random
from mixins import Duplicatable, Printable, Equalable
from mutate import mutate


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
        new_id = mutate(self.id)
        return Colicin(new_id)

    def __hash__(self):
        return hash(self.id)
