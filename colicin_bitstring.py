"""
a colicin is represented by a bitstring
immunity is represented by another bitstring
colicin binding to immunity is represented by the
hamming distance being less than
a proportion
"""
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
