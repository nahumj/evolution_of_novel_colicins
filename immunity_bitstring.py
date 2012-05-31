"""
a colicin is represented by a single bitstring
immunity is represented by another bitstring
"""
from mutate import mutate
from immunity import Immunity as ImmunityInt


class Immunity(ImmunityInt):

    def can_bind(self, colicin):
        dist = colicin.id.hamming_distance(self.id)
        return dist <= self.binding_range
