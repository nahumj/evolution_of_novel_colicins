"""
Module containing the logic for an Organism instance.
"""

import copy

from mixins import Duplicatable, Printable, Equalable


class Organism(Duplicatable, Printable, Equalable):
    """
    Holds colicin genes and immunity genes.
    """

    def __init__(self, colicins, immunities):
        self.colicins = colicins
        self.immunities = immunities

    def is_immune_to(self, colicin):
        """
        Returns true if one (or more) of the orgs Immunity genes
        can bind to the colicin.
        """
        return any(immunity.can_bind(colicin) for immunity
                in self.immunities)

    def is_self_toxic(self):
        """
        Returns true if one or more of the colicins produced by
        self can kill self.
        """
        return any(not self.is_immune_to(colicin) for colicin
                in self.colicins)

    def mutate(self):
        """
        Return a mutant with mutated colcins and immunities.
        """
        mutant_colicins = [col.mutate() for col in self.colicins]
        mutant_immunities = [imm.mutate() for imm in self.immunities]
        return Organism(mutant_colicins, mutant_immunities)
