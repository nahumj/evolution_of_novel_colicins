"""
This module implements a crude Bitstring with boolean values
in python tuples. Bitstring instances are immutable.
"""

class Bitstring(object):

    def __init__(self, iterable=None):
        if not iterable:
            iterable = []
        elif isinstance(iterable, str):
            self._value = tuple(char == "1" for char in iterable)
        else:
            self._value = tuple(bool(char) for char in iterable)

    def __len__(self):
        return len(self._value)

    def __getitem__(self, key):
        return self._value[key]

    def __iter__(self):
        return iter(self._value)

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        if len(self) != len(other):
            return False
        return all(self_pos == other_pos for (self_pos, other_pos)
                in zip(self, other))

    def __hash__(self):
        return hash(self._value)

    def __repr__(self):
        def bool_to_str(boolean):
            if boolean:
                return "1"
            return "0"

        value_as_string = "".join(
                bool_to_str(pos) for pos in self)
        return "{}({!r})".format(self.__class__.__name__, value_as_string)

    def hamming_distance(self, other):
        return len(tuple(None for (self_pos, other_pos)
                in zip(self, other) if self_pos != other_pos))


def from_iterable(iterable):
    t = tuple(bool(item) for item in iterable)
    b = Bitstring()
    b.value = t
    return b
