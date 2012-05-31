"""
a colicin is represented by a single bitstring
immunity is represented by another bitstring
"""
from mixins import Duplicatable, Printable, Equalable
from mutate import mutate


class Immunity(Duplicatable, Printable, Equalable):
    def __init__(self, id, binding_range):
        self.id = id
        self.binding_range = binding_range

    def can_bind(self, colicin):
        dist = colicin.id.hamming_distance(self.id)
        return dist <= self.binding_range

    def mutate(self):
        """
        Returns an immunity instance shifted by one
        (Binding range unchanged)
        """
        return Immunity(mutate(self.id), self.binding_range)
