"""
Module containing the logic for an Organism instance.
"""

import copy

class Organism(object):
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

    def duplicate(self):
        return copy.deepcopy(self)

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return (self.colicins == other.colicins and
                self.immunities == other.immunities)

    def __repr__(self):
        return "{}({!r}, {!r})".format(self.__class__.__name__, self.colicins, self.immunities)
